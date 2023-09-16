''' Prepare KITTI data for 3D object detection.
Author: Charles R. Qi
Date: September 2017
url: https://github.com/charlesq34/frustum-pointnets/blob/master/kitti/prepare_data.py
'''
from __future__ import print_function

import os
import struct
import glob
from scipy.spatial import ConvexHull
import sys
from kitti_object import *
import numpy as np
import cv2
import mayavi.mlab as mlab
from viz_util import draw_lidar, draw_lidar_simple, draw_gt_boxes3d
import keyboard
#from pytorch3d.ops import box3d_overlap

def in_hull(p, hull):
    from scipy.spatial import Delaunay
    if not isinstance(hull, Delaunay):
        hull = Delaunay(hull)
    return hull.find_simplex(p) >= 0


def extract_pc_in_box3d(pc, box3d):
    ''' pc: (N,3), box3d: (8,3) '''
    box3d_roi_inds = in_hull(pc[:, 0:3], box3d)
    return pc[box3d_roi_inds, :], box3d_roi_inds


def extract_pc_in_box2d(pc, box2d):
    ''' pc: (N,2), box2d: (xmin,ymin,xmax,ymax) '''
    box2d_corners = np.zeros((4, 2))
    box2d_corners[0, :] = [box2d[0], box2d[1]]
    box2d_corners[1, :] = [box2d[2], box2d[1]]
    box2d_corners[2, :] = [box2d[2], box2d[3]]
    box2d_corners[3, :] = [box2d[0], box2d[3]]
    box2d_roi_inds = in_hull(pc[:, 0:2], box2d_corners)
    return pc[box2d_roi_inds, :], box2d_roi_inds


def demo():
    file1 = open('C:\\Users\\Leandro\\Desktop\\Tese\\scripts\\valsplit.txt', 'r')
    Lines = file1.readlines()
    for line in Lines:
        data_idx = int(line)
        ROOT_DIR="D:\\kittitest\\object\\"
        PRED_DIR="D:\\kittitest\\eval\\result\\"
        dataset = kitti_object(ROOT_DIR)
        # Load data from dataset
        objects = dataset.get_label_objects(data_idx)
        objects_predicted = dataset.get_label_predicted_objects(data_idx,PRED_DIR)
        pc_velo = dataset.get_lidar(data_idx)[:, 0:3]
        calib = dataset.get_calibration(data_idx)

        NumberLabels=len(objects)
        CounterLine=0
        countNumberCar=0
        for countCar in objects:
            if countCar.type == 'Car':
                countNumberCar=countNumberCar+1

        print("NUMBER CARS GT: " + str(countNumberCar))

        CounterCorrect=0

        for obj in objects:
            CounterLine=CounterLine+1
            if obj.type != 'Car':
                continue
            else:

                print(' -------- GT bounding box --------')
                print(str(CounterLine)+"/"+str(countNumberCar))
                box3d_pts_2d, box3d_pts_3d = utils.compute_box_3d(obj, calib.P)
                box3d_pts_3d_velo = calib.project_rect_to_velo(box3d_pts_3d)
                box3droi_pc_velo, _ = extract_pc_in_box3d(pc_velo, box3d_pts_3d_velo)

                #intersection_vol, iou_3d = box3d_overal(boxes1, boxes2)
                GT_ObjectCoords=[obj.ymin,obj.xmin,obj.ymax,obj.xmax]

                currentIOU = 0
                BB3DOther=0
                bestFitPrediction=None
                for other_objs in objects_predicted:
                    _, box3d_pts_3d_other = utils.compute_box_3d(other_objs, calib.P)
                    box3d_pts_3d_velo_other = calib.project_rect_to_velo(box3d_pts_3d_other)

                    DT_ObjectCoords = [other_objs.ymin, other_objs.xmin, other_objs.ymax, other_objs.xmax]

                    ious =iou(GT_ObjectCoords,DT_ObjectCoords)
                    if ious > currentIOU and ious > 0.7:
                        currentIOU=ious
                        CounterCorrect=CounterCorrect+1
                        bestFitPrediction=other_objs
                        BB3DOther=box3d_pts_3d_velo_other

                print("IoU: " + str(currentIOU))

                #VISUALIZATION

                if(bestFitPrediction != None):
                    if(bestFitPrediction.type != obj.type):

                        fig = mlab.figure('Frame: '+str(data_idx), bgcolor=(0, 0, 0))
                        draw_lidar(box3droi_pc_velo, fig=fig)

                        draw_gt_boxes3d([box3d_pts_3d_velo], fig=fig, color=(0,1,0), draw_text=True, text_val=obj.type)
                        if currentIOU != 0:
                            draw_gt_boxes3d([BB3DOther], fig=fig, color=(1,0,0), draw_text=True,text_val=bestFitPrediction.type)

                        mlab.show()

    print("Correct: " + str(CounterCorrect))


def area(boxes, add1=False):

    if add1:
        return (boxes[2] - boxes[0] + 1.0) * (
            boxes[3] - boxes [1] + 1.0)
    else:
        return (boxes[2] - boxes[0]) * (boxes[3] - boxes[1])


def intersection(boxes1, boxes2, add1=False):

    [y_min1, x_min1, y_max1, x_max1] = [boxes1[0],boxes1[1],boxes1[2],boxes1[3]]
    [y_min2, x_min2, y_max2, x_max2] = [boxes2[0],boxes2[1],boxes2[2],boxes2[3]]

    all_pairs_min_ymax = np.minimum(y_max1, np.transpose(y_max2))
    all_pairs_max_ymin = np.maximum(y_min1, np.transpose(y_min2))
    if add1:
        all_pairs_min_ymax += 1.0
    intersect_heights = np.maximum(
        np.zeros(all_pairs_max_ymin.shape),
        all_pairs_min_ymax - all_pairs_max_ymin)

    all_pairs_min_xmax = np.minimum(x_max1, np.transpose(x_max2))
    all_pairs_max_xmin = np.maximum(x_min1, np.transpose(x_min2))
    if add1:
        all_pairs_min_xmax += 1.0
    intersect_widths = np.maximum(
        np.zeros(all_pairs_max_xmin.shape),
        all_pairs_min_xmax - all_pairs_max_xmin)
    return intersect_heights * intersect_widths


def iou(boxes1, boxes2, add1=False):

    intersect = intersection(boxes1, boxes2, add1)
    area1 = area(boxes1, add1)
    area2 = area(boxes2, add1)
    union = area1 + area2 - intersect
    return intersect / union

def main():
    demo()

if __name__ == "__main__":
    main()

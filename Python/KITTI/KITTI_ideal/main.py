''' Prepare KITTI data for 3D object detection.
Author: Charles R. Qi
Date: September 2017
url: https://github.com/charlesq34/frustum-pointnets/blob/master/kitti/prepare_data.py
'''
from __future__ import print_function

import os
import struct
import glob
import sys
from kitti_object import *
import numpy as np
import cv2
import mayavi.mlab as mlab
from viz_util import draw_lidar, draw_lidar_simple, draw_gt_boxes3d


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
    starting_frame=6284
    training_frames_number=7481
    for i in range(6284, training_frames_number, 1):
        data_idx = i
        ROOT_DIR="D:\\kittitest\\object\\"
        OUTPUT_DIR_VELO="E:\\KITTI\\velodyne_ideal\\"
        OUTPUT_DIR_PLY="E:\\KITTI\\newply\\"
        dataset = kitti_object(ROOT_DIR)
        # Load data from dataset
        objects = dataset.get_label_objects(data_idx)
        pc_velo = dataset.get_lidar(data_idx)[:, 0:3]
        calib = dataset.get_calibration(data_idx)

        tupleval = loadGtaVelodyneBinFile(ROOT_DIR + "training\\velodyne\\" + '%06d.bin' % (data_idx))

        IsCar=0

        for obj in objects:
            if obj.type != 'Car':
                continue
            else:
                IsCar=1
                print("A CAR")
                # Show LiDAR points that are in the 3d box
                print(' -------- LiDAR points in a 3D bounding box with object --------')
                box3d_pts_2d, box3d_pts_3d = utils.compute_box_3d(obj, calib.P)
                box3d_pts_3d_velo = calib.project_rect_to_velo(box3d_pts_3d)
                box3droi_pc_velo, _ = extract_pc_in_box3d(pc_velo, box3d_pts_3d_velo)

                #VISUALIZATION
                #fig = mlab.figure(figure=None, bgcolor=(0, 0, 0))
                #draw_lidar(box3droi_pc_velo, fig=fig)
                #draw_gt_boxes3d([box3d_pts_3d_velo], fig=fig)
                #mlab.show()


                tupleNew = addIntensityToPointCloud(tupleval, box3droi_pc_velo)
                tupleval=tupleNew

        if(IsCar):
            saveKittiVelodyneFile(tupleNew, OUTPUT_DIR_VELO + '%06d.bin' % (data_idx))
        else:
            saveKittiVelodyneFile(tupleval, OUTPUT_DIR_VELO + '%06d.bin' % (data_idx))

        output_path = OUTPUT_DIR_PLY + '%06d.ply' % (data_idx)
        values = loadKittiVelodyneFile(OUTPUT_DIR_VELO + '%06d.bin' % (data_idx))
        savePlyFile(output_path, values)




def loadGtaVelodyneBinFile(file_path):
    points = np.fromfile(file_path, dtype=np.float32).reshape(-1, 4)
    points = points[:, :4]  # exclude luminance

    point_tuple_list = []
    for i in range(len(points)):
        point_tuple_list.append((points[i][0], points[i][1], points[i][2], 0.0))

    return point_tuple_list

def addIntensityToPointCloud(tuple_list, box3droi_pc_velo):
    new_tuple_list = []

    for t in tuple_list:
        checkX=0
        checkY=0
        checkZ=0
        if t[0] in box3droi_pc_velo[:, 0]:
            checkX = 1
        if t[1] in box3droi_pc_velo[:, 1]:
            checkY = 1
        if t[2]  in box3droi_pc_velo[:, 2]:
            checkZ = 1

        if(checkX and checkY and checkZ):
            new_tuple_list.append((t[0], t[1], t[2], 1.0))
        else:
            new_tuple_list.append((t[0], t[1], t[2],t[3]))

    return new_tuple_list

def saveKittiVelodyneFile(tuple_list,directory):
    '''
    Saves pointcloud in binary file and is independent of the number of properties in the pointcloud points
    '''

    print("Directory: "+directory)
    with open(directory, "wb") as f:
        for point in tuple_list:
            s = struct.pack('f'*len(point), *point)
            f.write(s)


def loadKittiVelodyneFile(file_path, include_luminance=True):
    '''
    Loads a kitti velodyne file (ex: 000000.bin) into a list of tuples, where each tuple has (x, y, z) or (x, y, z, l)
    Right now it discards the 4th vaule of each point, i.e. the luminance
    Argument:
        - include_luminance: if the function should also store the pont intensisty value in the list of points
    '''
    # Source: https://github.com/hunse/kitti/blob/master/kitti/velodyne.py
    points = np.fromfile(file_path, dtype=np.float32).reshape(-1, 4)
    point_tuple_list = []

    if include_luminance:
        points = points[:, :4]  # exclude luminance

        for i in range(len(points)):
            point_tuple_list.append((points[i][0], points[i][1], points[i][2], points[i][3]))
    else:
        points = points[:, :3]  # exclude luminance

        for i in range(len(points)):
            point_tuple_list.append((points[i][0], points[i][1], points[i][2],))

    return point_tuple_list


def savePlyFile(filepath, tuple_list, attributes=None, color_for_every_point=(0, 255, 0)):
    '''
    For testing in the Main.py file
    Save list of points (possibly with attributes such as color) into a .PLY formated file
    Arguments:
        - tuple_list: list of points and their attributes
        - attributes: to indicate what type of attributes are included in the points:
            - c: each point has position + color (r, g, b)
    '''
    with open(filepath, "w") as the_file:
        header_lines = ["ply", "format ascii 1.0"]
        header_lines.append("element vertex " + str(len(tuple_list)))
        header_lines.append("property float x")
        header_lines.append("property float y")
        header_lines.append("property float z")
        header_lines.append("property float intensity")


        # if point have color
        if attributes == "c" or attributes == "i":
            header_lines.append("property uchar red")
            header_lines.append("property uchar green")
            header_lines.append("property uchar blue")

        header_lines.append("end_header")

        for i in range(0, len(header_lines)):
            the_file.write(header_lines[i] + "\n")

        for i in range(0, len(tuple_list)):
            if attributes == "c" and len(
                    tuple_list[i]) <= 3:  # if the points dont have color, but the attributes is set to "c"
                new_tuple = (tuple_list[i][0], tuple_list[i][1], tuple_list[i][2], color_for_every_point[0],
                             color_for_every_point[1], color_for_every_point[2])
                the_file.write(tupleToStr(new_tuple) + "\n")
            elif attributes == "i" and len(tuple_list[i]) == 4:
                # intensity values are between 0 and 1
                red_percent = int((1 - tuple_list[i][3]) * 255)
                green_percent = int(tuple_list[i][3] * 255)
                new_tuple = (tuple_list[i][0], tuple_list[i][1], tuple_list[i][2], red_percent, green_percent, 0)
                the_file.write(tupleToStr(new_tuple) + "\n")

            else:
                the_file.write(tupleToStr(tuple_list[i]) + "\n")


def tupleToStr(tuple):
    '''
    Converts a tuple of N size into a string, where each element is separated by a space.
    Arguments:
    - tuple: tuple to be converted into string
    Returns:
        - string with the tuple values
    '''
    tuple_string = ""
    for i in range(0, len(tuple)):
        if i == (len(tuple) - 1):
            tuple_string += str(tuple[i])
        else:
            tuple_string += str(tuple[i]) + " "

    return tuple_string

def main():
    demo()

if __name__ == "__main__":
    main()

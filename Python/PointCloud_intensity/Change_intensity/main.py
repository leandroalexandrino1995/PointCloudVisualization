import struct
import numpy as np
import glob
import os


def loadGtaVelodyneBinFile(file_path):
    points = np.fromfile(file_path, dtype=np.float32).reshape(-1, 4)
    points = points[:, :4]  # include luminance

    point_tuple_list = []
    for i in range(len(points)):
        point_tuple_list.append((points[i][0], points[i][1], points[i][2],points[i][3]))

    return point_tuple_list

def saveKittiVelodyneFile(tuple_list, filename, directory):
    '''
    Saves pointcloud in binary file and is independent of the number of properties in the pointcloud points
    '''

    with open(directory + filename, "wb") as f:
        for point in tuple_list:
            s = struct.pack('f'*len(point), *point)
            f.write(s)

def addIntensityToPointCloud(tuple_list, dummy_value):
    new_tuple_list = []
    for t in tuple_list:
        if(t[3] in dummy_value):
            new_tuple_list.append((t[0], t[1], t[2], t[3]))
        else:
            new_tuple_list.append((t[0], t[1], t[2], 0))
    return new_tuple_list

def main():

    for filesonpath in glob.glob("F:\\Testing_ALL\\velodyne_entity_prefix\\*.bin"):
        file_name = os.path.basename(filesonpath)
        file_split = file_name.split(".")
        file_label="F:\\Testing_ALL\\label_aug_2\\"+ file_split[0] +".txt"
        vehicle_set=set()
        with open(file_label) as f:
            for line in f:
                lineval = line.strip().split(' ')
                if (lineval[0] == 'Car'):
                    vehicle_set.add(float(lineval[15]))
                    #print("Entity ID car:" + lineval[15] + ". On frame: " + file_split[0])

        tupleval = loadGtaVelodyneBinFile(filesonpath)
        tuplenew = addIntensityToPointCloud(tupleval, vehicle_set)
        saveKittiVelodyneFile(tuplenew,file_split[0] + '.bin','F:\\Testing_ALL\\velodyne_entity\\')
        print("Done "+file_split[0])
    print("Operation finished!")

if __name__ == "__main__":
    main()

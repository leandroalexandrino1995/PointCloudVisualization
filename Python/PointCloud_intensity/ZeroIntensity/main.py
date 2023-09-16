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

def addIntensityToPointCloud(tuple_list, dummy_value = 0):
    new_tuple_list = []
    for t in tuple_list:
        if(t[3] > 0):
            new_tuple_list.append((t[0], t[1], t[2], 1.0))
        else:
            new_tuple_list.append((t[0], t[1], t[2], 0.0))

    return new_tuple_list

def main():
    listReplace = [772, 14952, 14832, 14833, 14878, 14882, 14748, 14747, 14461, 14197, 14918, 10345, 10281,
                   10082, 10083, 9875, 7813, 7782, 7783, 7784, 7785, 7786, 5741, 1821]

    for lstAd in range(1548,1680):
        listReplace.append(lstAd)

    for i in range(0, len(listReplace)):
        filename = '%06d' % (listReplace[i])
        file = "E:\\Dataset\\velodyne_velocity_abs\\" + filename + ".bin"
    #for filesonpath in glob.glob("E:\\Dataset\\velodyne_velocity_abs\\*.bin"):
    #    file_name = os.path.basename(filesonpath)
    #    file_split = file_name.split(".")
        tupleval = loadGtaVelodyneBinFile(file)
        tuplenew = addIntensityToPointCloud(tupleval, 0)
        saveKittiVelodyneFile(tuplenew,filename + '.bin','E:\\Dataset\\velodyne_velocity_abs_ideal\\')
        print("Done "+filename)
    print("Operation finished!")

if __name__ == "__main__":
    main()

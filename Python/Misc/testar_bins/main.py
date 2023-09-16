import numpy
import numpy as np

if __name__ == '__main__':
    pointcloud_range=numpy.array([0, -39.68, -3, 69.12, 39.68, 1])
    voxel=numpy.array([0.16, 0.16, 4])
    grid_size=(pointcloud_range[3:6]-pointcloud_range[0:3])/np.array(voxel)
    grid_size=np.round(grid_size).astype(np.int64)
    print(grid_size)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

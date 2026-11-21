# 1.Creating Numpy Arrays
import numpy as np
arr1D = np.arange(1,11)
arr2D = np.arange(1,10).reshape(3,3)
list = [10,20,30,40,50]
arrList = np.array(list)
print(arr1D)
print(arr2D)
print(arrList)
print(arr1D.shape)
print(arr2D.shape)
print(arrList.shape)
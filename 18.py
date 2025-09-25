# 1D array
import numpy as np
arr1=np.array([1,2,3,4,5])
print(arr1)

#2D array (matrix)
arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)

#3 Adding two array
import array
a = array.array('i',[1,2,3])
b = array.array('i',[4,5,6])
result=array.array('i',[a[i]+b[i]for i in range(len(a))])
print(result)


#4 using Numpy Array (vectorized):
import numpy as np
a = np.array([1,2,3])
b = np.array([4,5,6])
result=a+b
print(result)
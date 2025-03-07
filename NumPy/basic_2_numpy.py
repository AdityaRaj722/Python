# shape--dimension
# len-length of arrau
#  ndim- number of array dimension
#  size--number of array elemnts
# dtype-datatype of array elements
# astype(int)--convert  on array to a different type
import numpy as np
a=[[30,40,20],[40,60,50]]
arr=np.array(a)
print(arr)
print(type(arr))
print(arr.shape)
print(len(arr))
print(np.size(arr))
print(arr.dtype)
print(arr.astype(float))
# all the codes related to numpy
import numpy as np
a=np.array([20,30,40])
b=np.array([50,60,70])
print(a+b)
print(a*b)

# arr=np.array([[10,20,30,40],[50,70,80,90]])
# print(arr)
# print(type(arr))

# slicing
arr1=np.array([10,20,30,40])
# print(arr1[0:])
# print(arr1[3:])
# print(arr1[:3])

arr2=np.array([[10,20,30,40],[50,70,80,90],[15,18,40,57]])
# print(arr2[0:2,0:2])
# print(arr2[0,1:3])
# print(arr2[1,2:4])
# print(arr2[2,2:4])
# print(arr2[2,2])

print(np.shape(arr2))  # (rows ,coloums)
print(np.size(arr2)) # count all the elements
print(np.ndim(arr2))  #dimension 2d
print(arr2.dtype) #data type
import numpy as np
# arr1=np.array([30,40,50])
# arr2=np.array([5,5,3])
# print(np.concatenate([arr1,arr2]))

# arr1=np.array([[30,40],[60,50]])
# arr2=np.array([[5,5],[3,8]])
# print(np.concatenate([arr1,arr2],axis=1))
#
# print(np.hstack([arr1,arr2]))  # horizontal concatination
#
# print(np.vstack([arr1,arr2])) # verical conactination

a=np.array([20,30,40,50,60,70])
b=np.array_split(a,3)
print(b)
arr1=np.array([[20,30,40],[45,60,50]])
c=np.array_split(arr1,5)
print(c)
import numpy as np
# arr=np.array([[10,20],[30,40]])
# arr2=np.array([[40,80],[90,70]])

# print(arr+arr2)
# print(np.add(arr,arr2))
#
# print(arr-arr2)
# print(np.subtract(arr,arr2))
#
# print(arr/arr2)
# print(np.divide(arr,arr2))
#
# print(arr*arr2)
# print(np.multiply(arr,arr2))

# arr=np.array([3,4,2,6])
# arr2=np.array([3])
# print(np.pow(arr,arr2))
#
# arr3=np.array([ 25 ,64 ,  16, 256])
#
# print(np.sqrt(arr3))


#  adding removing in array
# arr=np.array([20,40,60,80])
# arr1=np.array([[20,40],[60,80]])
# print(np.append(arr,90))
# print(np.append(arr1,[89,78]))
#
# print(np.insert(arr,1,50))
# print(np.insert(arr1,1,[50,78],axis=1))
#
# print(np.delete(arr,1))
# print(np.delete(arr1,1,axis=1))


# aggreate functins array
# a=np.array([20,40,30,50])
# print(np.sum(a))
# print(np.min(a))
# print(np.max(a))
# print(np.size(a))
# print(np.mean(a))
# print(np.cumsum(a))
# print(np.cumprod(a))

# a=[100,150,199,200,250,130]
# b=[10,50,30,40,30,10]
#
# price=np.array(a)
# quantity=np.array(b)
# # print(price,quantity)
# c=np.cumprod([price,quantity],axis=0)
# print(np.sum(c[1]))


# statistical functions
import statistics as stats
backed_food=[200,300,150,130,200,280,170,188]
a=np.array(backed_food)
print(np.mean(a))  # sum of all the vlaues /numbes of values
print(np.median(a))  # sort and cerntral vlaue
print(np.sort(a))
print(stats.mode(a))
print(np.std(a))
print(np.var(a))

tobacco_consumiton=[30,50,10,30,50,40]
deaths=[100,120,70,100,120,112]
print(np.corrcoef([tobacco_consumiton,deaths]) )
#-1 represent  inversely proportional relationship
#1 represent   proportional relationship
#0 means no relationship


price=[300,100,350,150,200]
sales=[10,20,7,17,3]
print(np.corrcoef([price,sales]))


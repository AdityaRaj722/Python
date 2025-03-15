import matplotlib.pyplot as plt
import numpy as np
import  pandas as pd

x=[1,2,3,4,5]
y=[45,67,33,67,12]
y1=[41,30,13,66,13]
y2=[11,30,55,60,19]
y3=[11,40,65,90,69]

plt.figure(figsize=[5,3])
plt.plot(x,y,label="male")
plt.plot(x,y1,label="Female")
plt.plot(x,y2,label="children")
plt.plot(x,y3,label="blanks")
# plt.legend(["a1","a2""a3"],ncols=2)
plt.legend(bbox_to_anchor=(0.8,1.2),ncols=2)
plt.show()

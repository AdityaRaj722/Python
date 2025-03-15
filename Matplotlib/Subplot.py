import matplotlib.pyplot as plt
import numpy as np
import  pandas as pd

x=[1,2,3,4,5]
y=[45,64,48,25,33]
plt.subplot(1,2,1)
plt.title("Age")
plt.plot(x,y)

x=[5,6,7,8,9]
y=[67,50,65,66,89]
plt.subplot(1,2,2)
plt.title("Weight")
plt.plot(x,y)
plt.suptitle("Employee Data")
plt.show()
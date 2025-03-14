import matplotlib.pyplot as plt
import numpy as np
import  pandas as pd

# days=[1,2,3,4,5,6,7]
#
# NOP1=[5,10,30,20,35,60,80]
# NOP2=[10,40,30,85,70,90,90]
# NOP3=[8,30,50,60,70,90,100]
#
# plt.stackplot(days,NOP1,NOP2,NOP3,colors=["pink","blue","red"],labels=["Week1","Week2","Week3"])
# plt.legend()
# plt.show()



data=pd.read_csv("food_data.csv")
df=pd.DataFrame(data)
print(df)

import matplotlib.pyplot as plt
import numpy as np
import  pandas as pd

# brands=["OnePlus","Samsung","Apple","Nokia","Redmi"]
# x=[22,25,30,3,10]
# c=["red","blue","green","pink","black"]
# ex=[0,0,0,0,1]
# plt.pie(x,labels=brands,colors=c,explode=ex,shadow=True,autopct="%.2f",startangle=90)
# plt.show()

data=pd.read_excel("expense3.xlsx")
df=pd.DataFrame(data)
print(df)
grouped_by=df.groupby("Payment Mode")["Amount"].sum()
print(grouped_by)
plt.pie(grouped_by.values,labels=grouped_by.index,autopct="%.2f")
plt.savefig("pie.png",facecolor="black",pad_inches=0.2,bbox_inches="tight")
plt.show()
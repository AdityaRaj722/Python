import matplotlib.pyplot as plt
import numpy as np
import  pandas as pd

# x=["Day1","Day2","Day3","Day4","Day5"]
# y=[30,40,25,30,40]
# plt.step(x,y,where="post",marker='o')
# plt.show()


data=pd.read_excel("expense3.xlsx")
df=pd.DataFrame(data)
print(df)
grouped=df.groupby("Category").agg({"Amount":"sum"})
plt.step(grouped.index,grouped["Amount"],where="mid",marker='o')
plt.show()
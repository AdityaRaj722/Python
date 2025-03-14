import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# x=np.random.randint(1,10,50)
# y=np.random.randint(10,100,50)
# color=np.random.randint(10,100,50)
#
# plt.scatter(x,y,marker="*",cmap="viridis",c=color)
# plt.colorbar()
# plt.show()

data=pd.read_excel("ESD.xlsx")
df=pd.DataFrame(data)
print(df)
plt.scatter(df["Annual Salary"],df["EEID"],s=df["Age"])
plt.show()

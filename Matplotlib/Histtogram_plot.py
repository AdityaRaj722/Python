import matplotlib.pyplot as plt
import numpy as np
import  pandas as pd

# x=[30,40,68,27,47,59,47,88,44,23,44,66,66,33,5,2,5,50]
# plt.hist(x,bins=15,edgecolor="black",color="purple")
# plt.show()


data=pd.read_excel("ESD.xlsx")
df=pd.DataFrame(data)
print(df)
plt.hist(df["Age"],bins=15)
plt.show()
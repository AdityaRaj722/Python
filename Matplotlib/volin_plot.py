import matplotlib.pyplot as plt
import numpy as np
import  pandas as pd

# a=[30,40,68,27,47,59,47,88,44,23,44,66,66,33,5,2,5,50]
# plt.violinplot(a,showmeans=True)
# plt.show()


data=pd.read_excel("ESD.xlsx")
df=pd.DataFrame(data)
print(df)
plt.violinplot(df["Annual Salary"],showmeans=True)
plt.show()
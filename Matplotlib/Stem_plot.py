import matplotlib.pyplot as plt
import numpy as np
import  pandas as pd

# x=[30,40,68,27,47,59,47,88,44,23,44,66,66,33,5,2,5,50]
# plt.stem(x,linefmt="--",markerfmt="D",bottom=10,orientation='horizontal')
# plt.show()


data=pd.read_excel("ESD.xlsx")
df=pd.DataFrame(data)
df2=df.head(50)
print(df2)
plt.stem(df2["Age"])
plt.plot(df2["Age"])
plt.show()
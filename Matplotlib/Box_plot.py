import matplotlib.pyplot as plt
import numpy as np
import  pandas as pd

# l=[25,46,57,25,45,13,29,39,46,99,22,12,14,16,55,6,46,52,55,78]
# l2=[1,3,4,7,12,2,8,9,24]
# plot_val=[l,l2]
# plt.boxplot(plot_val)
# plt.show()

data=pd.read_excel("expense3.xlsx")
df=pd.DataFrame(data)
print(df)
plt.boxplot(df["Amount"])
plt.show()
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data=sns.load_dataset("tips")
print(data)
sns.violinplot(data,x="total_bill")
plt.show()
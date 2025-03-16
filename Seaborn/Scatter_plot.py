import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data=sns.load_dataset("tips")
print(data)
sns.scatterplot(data,x="total_bill",y="tip",hue="smoker",size="size",palette="viridis")
plt.show()
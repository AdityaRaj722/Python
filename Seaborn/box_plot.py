import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data=sns.load_dataset("tips")
sns.boxplot(data,x="sex",y="tip",orient='vertical')
plt.show()
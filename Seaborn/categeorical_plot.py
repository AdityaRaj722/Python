import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data=sns.load_dataset("tips")

sns.catplot(x="day",y="tip",data=data,hue="sex",kind="violin")
plt.show()
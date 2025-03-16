import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data=sns.load_dataset("tips")

sns.stripplot(data,x="day",y="total_bill",hue="sex",dodge=True,jitter=0.3)
plt.show()

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data=sns.load_dataset("tips")
gp=data.groupby("day").agg({"tip":"mean"})
sns.heatmap(gp)
plt.show()
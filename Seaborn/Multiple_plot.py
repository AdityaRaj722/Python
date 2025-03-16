import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data=sns.load_dataset("tips")
print(data)

a=sns.FacetGrid(data,col="time",height=2,hue="sex")
a.map(sns.barplot,"day","tip")
plt.show()
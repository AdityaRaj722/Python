import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data=sns.load_dataset("tips")

sns.kdeplot(data=data,x="total_bill",hue="day",multiple='stack')
plt.show()
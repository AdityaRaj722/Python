import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# data=sns.load_dataset("tips")
# sns.histplot(data,x="day",hue="sex",kde=True)
# plt.show()

data=sns.load_dataset("titanic")
print(data)

sns.histplot(data,x="age",hue="who",kde=True)
plt.show()
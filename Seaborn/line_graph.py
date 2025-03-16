import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
# data={"Days":[1,2,3,4,5],
#       "NOP":[50,40,60,30,44]}
# df=pd.DataFrame(data)
# print(df)
#
# sns.lineplot(data=data,x="Days",y="NOP")
# plt.show()

data=pd.read_excel("ESD.xlsx")
print(data)
color=sns.colors_pallet("viridis")
sns.lineplot(data=data,x="Business Unit",y="Age",hue="Gender")
plt.show()
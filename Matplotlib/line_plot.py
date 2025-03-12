import matplotlib.pyplot as plt
# x=["day1","day2","day3","day4","day5"]
# y=[300,450,250,230,400]
# y1=[500,450,300,250,320]
# plt.plot(x,y,marker="o",ls=":",color="red",label="week1")
# plt.plot(x,y1,marker="o",ls="--",color="blue",label="week2",alpha=0.5)
# plt.legend()
# plt.show()

import pandas as pd
data=pd.read_excel("expense3.xlsx")
df=pd.DataFrame(data)
print(df)
grouped_by=df.groupby("Category")["Amount"].sum()
print(grouped_by)
# plt.plot(df["Date"],df["Amount"])
plt.plot(grouped_by.index,grouped_by.values)
plt.show()
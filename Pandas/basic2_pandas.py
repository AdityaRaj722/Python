import pandas as pd

# exploring data in pandas
# data=pd.read_excel("expense3.xlsx")
# print(data)
data=pd.read_excel("ESD.xlsx")
# for showing starting 10 rows
# print(data)
# print(data.head(10))  #default it will print 5 values
# print(data.tail(10))

# print(data.info)
#
# print(data.describe())

print(data.isnull().sum())
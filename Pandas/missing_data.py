import numpy as np
import pandas as pd
data=pd.read_csv("company1.csv")
# print(data)
# print(data.isnull().sum()) # count of null values in each rows

# print(data.dropna())  # drop all rows and columns contaning nul vlaues

#  fill all the null values
# print(data.replace(np.nan,"hi"))

# data["salary"]=data["salary"].replace(np.nan,30000)
# print(data)

# avg_sal=data["salary"].mean()
# data["salary"]=data["salary"].replace(np.nan,avg_sal)
# print(data)

# fillna uses specific method to fill the null values
print(data.fillna(method="bfill"))  #backward fill
print(data.fillna(method="ffill")) # forward fill
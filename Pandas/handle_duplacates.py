import pandas as pd
data =pd.read_csv("company1.csv")
# print(data)
# checking duplicayte values
print(data['EEID'].duplicated().sum())

print(data.drop_duplicates("EEID"))
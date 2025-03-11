import pandas as pd

data=pd.read_excel("ESD.xlsx")
# print(data)
# print(data.head(10))

gp=data.groupby("Department",).agg({"EEID":"count"})
gp1=data.groupby("Job Title",).agg({"EEID":"count"})
gp2=data.groupby(["Department","Gender"]).agg({"EEID":"count"})
# print(gp)
# print(gp1)
# print(gp2)

gp3=data.groupby("Country").agg({"Age":"mean"})
gp4=data.groupby("Country").agg({"Annual Salary":"mean"})
gp5=data.groupby(["Country","Gender"]).agg({"Annual Salary":"max","Age":"min"})
print(gp5)
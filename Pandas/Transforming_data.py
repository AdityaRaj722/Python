import pandas as pd

df=pd.read_excel("ESD.xlsx")
# print(df)
# loc == lock
df.loc[(df["Bonus %"]==0),"GetBonus"] = "no bonus"
df.loc[(df["Bonus %"] > 0,"GetBonus")]="bonus"
# print(df.head(10))

# way to combine first name and last name in new column
# data["Full Name"]=data["First Name"].str.capatalise() + " "+data["Last Name"]

data=pd.read_excel("practice_1.xlsx")
data["Bonus"]=(data["Salary"]/100)*20
# print(data)

data2={"Months":["January","February","march","April"]}

a=pd.DataFrame(data2)
print(a)
def extraxt(value):
    return value[0:3]
a["Short_months"]=a["Months"].map(extraxt)
print(a)
import pandas as pd
data1={"Emp Id":["E01","E02","E03","E04","E05","E06"],
       "Name":["Ram","Shyam","Rahul","Vishal","Ravi","Das"],
       "Age":[34,41,25,17,47,78]}
data3={"Emp Id":["E07","E08","E09","E10","E11","E12"],
       "Name":["Aam","Naaam","Rum","Vishnu","Ramu","Dasi"],
       "Age":[34,41,25,17,47,78]}
data2={"Emp Id":["E01","E07","E03","E04","E08","E06"],
       "Salary":[45000,74000,29000,74000,87000,75000]}

df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)
df3=pd.DataFrame(data3)
# print(df1)
# print()
# print(df2)

# print(pd.merge(df1,df2,on="Emp Id"))

b=pd.merge(left=df1,right=df2,on="Emp Id",how="left")
c=pd.merge(left=df1,right=df2,on="Emp Id",how="right")
# print(b)
# print(c)

# join
d=pd.concat([df1,df3])
print(d)
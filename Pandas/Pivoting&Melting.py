import pandas as pd
dict={"Key":["k1","k2","k1","k2"],
      "Names":["Jhon","Ben","David","Peter"],
      "Houses":["Red","Blue","Green","Red"]}
df=pd.DataFrame(dict)
print(df)
# pivoting
a=df.pivot(index="Key", columns="Names", values="Houses")
# print(a)

# melting
dict1={"Names":["Jhon","Ben","David","Peter"],
      "Houses":["Red","Blue","Green","Red"],
      "Grades":["3rd","8th","9th","8th"]}

df2=pd.DataFrame(dict1)
# print(df2)

b=pd.melt(df2,id_vars=["Names"],value_vars=["Houses","Grades"],var_name="Houses&Grades",value_name="Values ")
print(b)
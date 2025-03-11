import pandas as pd

dict={"Fruits":["mango","apple","grapes","banana"],
      "Price":[150,100,80,30],
      "Quantity":[15,10,30,15]}

df=pd.DataFrame(dict)
# print(df)

df2=df.copy()
df2.loc[0,"Price"]=200
df2.loc[1,"Price"]=120
df2.loc[3,"Price"]=60
df2.loc[0,"Quantity"]=18
df2.loc[1,"Quantity"]=12
df2.loc[3,"Quantity"]=20

print(df2)
# print(df.compare(df2,align_axis=1))
# print(df.compare(df2,keep_equal=True))
print(df.compare(df2,keep_shape=True))
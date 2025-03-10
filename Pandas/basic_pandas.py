import pandas as pd

# panel data or python data analysis

# data framing
data={"Name":["Adi","Jhon","Lisa"],
      "Age":[25,28,31],
      "Salary":[30000,40000,45672]}

df=pd.DataFrame(data)
print(df)
# if i have a csf file or a data set and convert backward slash to forward if file in another folder

# data=pd.read_csv("customer_csv")
# data=pd.read_excel("file name with extension")
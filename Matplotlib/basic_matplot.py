# use  for graphical representation of info using data
# jhon D. hunter
# import matplotlib.pyplot as plt
# plotting of bar chart uisng given data
# y=[98,67,88,95,88]
# x=["Part1","Part2","Part3","Part4","Part5"]
# color=["red","green","blue","orange","blue"]
# plt.bar(x,y,color=color,edgecolor="black")
# plt.xlabel("Parts of Harry Potter")
# plt.ylabel("Popularity",fontsize=12)
# plt.title("Popularity of different parts if Harry Potter")
# plt.show()

# plotting using existing data uisng pandas
import pandas as pd
import matplotlib.pyplot as plt

# Read Excel file
data = pd.read_excel("expense3.xlsx")

# Create DataFrame
df = pd.DataFrame(data)
# print(df)

# Plot bar chart
grouped_by=df.groupby("Payment Mode")["Amount"].sum()
# plt.bar(df["Payment Mode"], df["Amount"], color='skyblue')
print(grouped_by)

plt.bar(grouped_by.index,grouped_by.values)

# Labeling
plt.xlabel("Payment Mode")
plt.ylabel("Amount Spent")
plt.title("Expenses by Payment Mode")

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

plt.savefig("bar.png")
# Show plot
plt.show()

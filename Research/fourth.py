import matplotlib.pyplot as plt

# Data
categories = ['Infrastructure', 'Operational', 'Energy Savings', 'Traffic Savings', 'Other Benefits']
percentages = [40, 30, 15, 10, 5]

# Plotting
plt.pie(percentages, labels=categories, autopct='%1.1f%%', startangle=90)
plt.title('Cost-Benefit Analysis of IoT and 5G Deployment')
plt.show()
# While infrastructure costs are high, energy and traffic savings provide significant long-term benefits.
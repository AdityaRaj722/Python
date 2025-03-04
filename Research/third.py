# import matplotlib.pyplot as plt
#
# # Data
# latency = [10, 20, 30, 40, 50]
# data_rates_4g = [50, 45, 40, 35, 30]
# data_rates_5g = [100, 200, 300, 400, 500]
#
# # Plotting
# plt.scatter(latency, data_rates_4g, label='4G', color='blue')
# plt.scatter(latency, data_rates_5g, label='5G', color='red')
# plt.xlabel('Latency (ms)')
# plt.ylabel('Data Rates (Mbps)')
# plt.title('5G vs. 4G Latency Comparison')
# plt.legend()
# plt.grid()
# plt.show()
# # 5G networks demonstrate 50% lower latency and higher data rates compared to 4G.

import matplotlib.pyplot as plt

# Data
categories = ['Infrastructure', 'Operational', 'Energy Savings', 'Traffic Savings', 'Other Benefits']
percentages = [40, 30, 15, 10, 5]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Plotting
plt.figure(figsize=(8, 6))
plt.pie(percentages, labels=categories, colors=colors, autopct='%1.1f%%', startangle=90, explode=(0.1, 0, 0, 0, 0))
plt.title('Cost-Benefit Analysis of IoT and 5G Deployment', fontsize=16)
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
plt.show()
# import matplotlib.pyplot as plt
# import numpy as np
#
# # Data
# months = ['January', 'February', 'March', 'April', 'May']
# before = [5000, 5100, 4900, 5200, 5300]
# after = [4500, 4400, 4300, 4200, 4100]
#
# # Plotting
# x = np.arange(len(months))
# plt.bar(x - 0.2, before, width=0.4, label='Before IoT & 5G')
# plt.bar(x + 0.2, after, width=0.4, label='After IoT & 5G')
# plt.xlabel('Months')
# plt.ylabel('Energy Consumption (kWh)')
# plt.title('Energy Consumption Comparison')
# plt.xticks(x, months)
# plt.legend()
# plt.show()
# # Energy consumption decreased by an average of 15% after IoT and 5G integration

import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May']
traffic_before = [100, 110, 105, 120, 115]  # Traffic flow before IoT & 5G
traffic_after = [90, 85, 80, 75, 70]  # Traffic flow after IoT & 5G

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(months, traffic_before, label='Before IoT & 5G', marker='o', color='blue', linewidth=2)
plt.plot(months, traffic_after, label='After IoT & 5G', marker='o', color='green', linewidth=2)
plt.xlabel('Months', fontsize=14)
plt.ylabel('Traffic Flow (Vehicles/Hour)', fontsize=14)
plt.title('Traffic Congestion Reduction Over Time', fontsize=16)
plt.legend(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()
import matplotlib.pyplot as plt

# Data
sectors = ['Energy', 'Transportation', 'Waste Management', 'Public Safety', 'Healthcare']
devices = [5000, 4000, 3000, 2000, 1000]

# Plotting
plt.bar(sectors, devices, color='skyblue')
plt.xlabel('Sectors')
plt.ylabel('Number of IoT Devices')
plt.title('IoT Device Deployment in Smart Cities')
plt.show()
# The energy sector has the highest number of IoT devices, followed by transportation and waste management.
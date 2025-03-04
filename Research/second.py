import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May']
before = [100, 110, 105, 120, 115]
after = [90, 85, 80, 75, 70]

# Plotting
plt.plot(months, before, label='Before IoT & 5G', marker='o')
plt.plot(months, after, label='After IoT & 5G', marker='o')
plt.xlabel('Months')
plt.ylabel('Traffic Flow (Vehicles/Hour)')
plt.title('Traffic Congestion Reduction Over Time')
plt.legend()
plt.grid()
plt.show()
# To show the reduction in traffic congestion after implementing IoT-enabled smart traffic systems.
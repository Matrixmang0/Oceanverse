import matplotlib.pyplot as plt

# Data
bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 500, 1000]
balls_required = [25, 60, 100, 128, 169, 254, 273, 308, 396, 480, 3120, 6201]

# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(bins, balls_required, color='blue', marker='o')
plt.title('Bins vs. Balls Required')
plt.xlabel('Number of Bins')
plt.ylabel('Balls Required')
plt.grid(True)
plt.savefig('Balls_vs_Bins.png')
plt.show()
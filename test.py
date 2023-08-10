import matplotlib.pyplot as plt

# Example data for SlowK and SlowD values (replace these with your actual data)
actual_slowk_values = [80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 10, 15, 20, 25,
                30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 85, 80, 75, 70, 65, 60, 55,
                50, 45, 40, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 85, 80, 75, 70, 65,
                60, 55, 50, 45, 40, 35, 30, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85,
                90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 20, 25, 30, 35,
                40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]

actual_slowd_values = [60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 10, 15, 20, 25, 30, 35, 40, 45,
                50, 55, 60, 65, 70, 75, 80, 85, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35,
                40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45,
                40, 35, 30, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 85, 80, 75,
                70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 20, 25, 30, 35, 40, 45, 50, 55,
                60, 65, 70, 75, 80, 85, 90, 95]

slowk_values = actual_slowk_values[:100]
slowd_values = actual_slowd_values[:100]
# Generating x-axis values (you may replace these with your date or time data)
x_values = list(range(1, 101))

# Plotting SlowK and SlowD
plt.figure(figsize=(10, 6))
plt.plot(x_values, slowk_values, label='SlowK', color='blue')
plt.plot(x_values, slowd_values, label='SlowD', color='red')

# Adding buy and sell signals using the condition for crossovers
for i in range(1, len(slowk_values)):
    if slowk_values[i] > slowd_values[i] and slowk_values[i - 1] <= slowd_values[i - 1]:
        plt.scatter(x_values[i-1], slowk_values[i-1], color='black', marker='^', s=100, zorder=5)
    elif slowk_values[i] < slowd_values[i] and slowk_values[i - 1] >= slowd_values[i - 1]:
        plt.scatter(x_values[i-1], slowk_values[i-1], color='black', marker='v', s=100, zorder=5)

plt.xlabel('Data Points')
plt.ylabel('Values')
plt.title('SlowK and SlowD with Buy and Sell Signals')
plt.legend()
plt.grid(True)
plt.show()
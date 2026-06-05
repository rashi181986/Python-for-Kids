import matplotlib.pyplot as plt
import pandas as pd

# 1. Setup the data (Sampled from your image)
data = {
    'month': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'profit': [211000, 183300, 224700, 222700, 209600, 201400, 295500, 361400, 234000, 266700, 412800, 300200],
    'toothpaste': [5200, 5100, 4550, 5870, 4560, 4890, 4780, 5860, 6100, 8300, 7300, 7400],
    'shampoo': [1200, 2100, 3550, 1870, 1560, 1890, 1780, 2860, 2100, 2300, 2400, 1800]
}
df = pd.DataFrame(data)

# 2. Create the plot
plt.figure(figsize=(10, 5))

# Plotting Total Profit
plt.plot(df['month'], df['profit'], label='Total Profit', color='red', marker='o', linewidth=3)

# Adding labels and title
plt.title('Company Profit Per Month')
plt.xlabel('Month Number')
plt.ylabel('Profit in Dollars')
plt.xticks(df['month']) # Ensure every month shows on the x-axis
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

plt.show()

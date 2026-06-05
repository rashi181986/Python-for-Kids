import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Loading & Cleaning (Pandas)
df = pd.read_csv('tips.csv')

# Add a 'tip_percentage' column
df['tip_pct'] = (df['tip'] / df['total_bill']) * 100

# 2. Mathematical Analysis (NumPy)
# Find the average tip for lunch vs dinner using NumPy logic
avg_tip = np.mean(df['tip'])
max_bill = np.max(df['total_bill'])

print(f"Dataset Overview:\n{df.head(3)}\n")
print(f"Average Tip: ${avg_tip:.2f}")
print(f"Highest Bill: ${max_bill:.2f}")
print("-" * 30)

# 3. Statistical Grouping (Pandas)
# Group by Day to see who gives the best tips
day_analysis = df.groupby('day')[['total_bill', 'tip']].median()
print("Median Bill & Tip per Day:")
print(day_analysis)

# 4. Basic Visualization (Matplotlib)
plt.figure(figsize=(8, 5))
plt.hist(df['total_bill'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Total Bills')
plt.xlabel('Bill Amount ($)')
plt.ylabel('Frequency')
plt.show()

# 5. Advanced Visualization (Seaborn)
# Using a Violin plot to see the density of tips across different days
plt.figure(figsize=(10, 6))
sns.violinplot(data=df, x='day', y='total_bill', hue='sex', split=True, palette='Pastel1')
plt.title('Bill Distribution by Day and Gender')
sns.despine() # Clean up the chart borders
plt.show()

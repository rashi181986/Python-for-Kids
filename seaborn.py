import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Creating a subset of your data for the visualization
data = {
    'month_number': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'facecream': [2500, 2630, 2140, 3400, 3600, 2760, 2980, 3700, 3540, 1990, 2340, 2900],
    'facewash': [1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760],
    'bathingsoap': [9200, 6100, 9550, 8870, 7760, 7490, 8980, 9960, 8100, 10300, 13300, 14400],
    'total_profit': [211000, 183300, 224700, 222700, 209600, 201400, 295500, 361400, 234000, 266700, 412800, 300200]
}
df = pd.DataFrame(data)

# Setting the visual style
sns.set_theme(style="whitegrid")

# 1. Regression Plot: Relationship between Bathing Soap and Total Profit
plt.figure(figsize=(10, 5))
sns.regplot(data=df, x='bathingsoap', y='total_profit', color='teal')
plt.title('Impact of Bathing Soap Sales on Total Profit')
plt.show()

# 2. Comparison: Distribution of Facecream vs Facewash
# We "melt" the data to make it compatible with Seaborn's categorical plots
df_melted = df.melt(id_vars='month_number', value_vars=['facecream', 'facewash'], 
                    var_name='Product', value_name='Sales')

plt.figure(figsize=(10, 5))
sns.barplot(data=df_melted, x='month_number', y='Sales', hue='Product')
plt.title('Monthly Sales Comparison: Facecream vs Facewash')
plt.show()

# 3. Correlation Heatmap: See how products relate to each other
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Product Correlation Matrix')
plt.show()

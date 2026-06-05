import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset (Assuming the file is in your current directory)
df = pd.read_csv('company_sales_data.csv')

# Set the aesthetics
sns.set_theme(style="white")

# 1. Pair Plot: Visualize pairwise relationships across all products
# This creates a matrix of scatter plots and histograms for the entire dataset
products_df = df[['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']]
sns.pairplot(products_df, corner=True, diag_kind='kde', plot_kws={'alpha': 0.6})
plt.suptitle('Pairwise Relationships Between Products', y=1.02)
plt.show()

# 2. Joint Plot: Focus on two variables with distributions
# Showing the relationship between Bathing Soap sales and Total Profit with a regression line
sns.jointplot(data=df, x='bathingsoap', y='total_profit', kind='reg', color='m', height=7)
plt.show()

# 3. Violin Plot: Distribution and density of sales for each product
# We melt the data to compare all product distributions side-by-side
melted_df = df.melt(id_vars=['month_number'], 
                    value_vars=['facecream', 'facewash', 'toothpaste', 'shampoo', 'moisturizer'],
                    var_name='Product', value_name='Sales')

plt.figure(figsize=(12, 6))
sns.violinplot(data=melted_df, x='Product', y='Sales', palette='muted', inner='quartile')
plt.title('Sales Distribution Density per Product')
plt.show()

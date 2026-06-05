import pandas as pd
import numpy as np

# 1. Create the DataFrame based on your image
data = {
    'Id': [1, 2, 3, 4],
    'Name': ['Pankaj', 'Meghna', 'David', 'Lisa'],
    'Role': ['CEO', np.nan, np.nan, np.nan],
    'Salary': [100, 200, np.nan, np.nan]
}

df = pd.DataFrame(data)

print("--- Original Data ---")
print(df)

# 2. Handling Missing Values (Data Cleaning)
# Fill missing Roles with 'Employee' and Salaries with the average (mean)
df['Role'] = df['Role'].fillna('Employee')
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())

# 3. Data Manipulation
# Add a new column for a 10% Bonus
df['Bonus'] = df['Salary'] * 0.10

# Calculate Total Compensation
df['Total'] = df['Salary'] + df['Bonus']

# 4. Filtering
# Show only people with a Salary greater than 120
high_earners = df[df['Salary'] > 120]

print("\n--- Processed Data ---")
print(df)

print("\n--- High Earners (> 120) ---")
print(high_earners)

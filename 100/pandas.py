import pandas as pd

# 1. How would you use Python for data cleaning? Provide examples using pandas.
data = pd.read_csv('raw_data.csv')

df = pd.DataFrame(data)

# Fill missing values in 'Name' column with a default value
df['Name'].fillna('Unknown', inplace=True)

# Replace 'not available' with NaN in 'Salary' and convert to numeric
df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')

# Fill missing 'Age' values with the mean age
df['Age'].fillna(df['Age'].mean(), inplace=True)

# Drop rows where Salary is still NaN
df.dropna(subset=['Salary'], inplace=True)

print(df)






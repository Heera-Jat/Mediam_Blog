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


# Q2 Explain the difference between loc[] and iloc[] in Pandas.

# Using loc to select rows by label
print(df.loc[0])  # Select first row by label
print(df.loc[:, 'Age'])  # Select 'Age' column by label

# Using iloc to select rows by index position
print(df.iloc[0])  # Select first row by index position
print(df.iloc[:, 1])  # Select second column by index position



# Q3 What is the difference between apply(), map(), and applymap() in Pandas?
import pandas as pd

# Sample DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# Using apply() to sum across rows
row_sum = df.apply(sum, axis=1)

# Using map() to square elements in a Series
df['A'] = df['A'].map(lambda x: x**2)

# Using applymap() to add 1 to every element in the DataFrame
df = df.applymap(lambda x: x + 1)

print(df)
print(row_sum)

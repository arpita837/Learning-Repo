import pandas as pd
# Create a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'City': ['New York', 'London', 'Paris', 'Sydney']
}
df = pd.DataFrame(data)
print(df)

# Accessing columns
names = df['Name']
ages = df.Age
print(names)
print(ages)

# Accessing rows by index
row2 = df.loc[1]
print(row2)

# Accessing rows by position
first_row = df.iloc[0]
print(first_row)

# Getting summary statistics
summary_stats = df.describe()
print(summary_stats)
# Reading data from a CSV file
csv_df = pd.read_csv('data.csv')
print(csv_df)

# Writing data to a CSV file
df.to_csv('output.csv', index=False)

# Reading data from an Excel file
excel_df = pd.read_excel('data.xlsx')
print(excel_df)

# Writing data to an Excel file
df.to_excel('output.xlsx', index=False)
# Filtering data based on conditions
filtered_df = df[df['Age'] > 28]
print(filtered_df)

# Adding a new column
df['Gender'] = ['Female', 'Male', 'Male', 'Male']
print(df)

# Grouping and aggregation
grouped_df = df.groupby('Gender')['Age'].mean()
print(grouped_df)

# Sorting the DataFrame
sorted_df = df.sort_values(by='Age', ascending=False)
print(sorted_df)
# Creating a DataFrame with missing values
data = {
    'A': [1, 2, None, 4, 5],
    'B': [None, 10, 20, 30, 40],
    'C': [100, 200, 300, None, 500]
}
df_missing = pd.DataFrame(data)
print(df_missing)

# Checking for missing values
print(df_missing.isnull())

# Dropping rows with missing values
df_cleaned = df_missing.dropna()
print(df_cleaned)

# Filling missing values with a specific value
df_filled = df_missing.fillna(0)
print(df_filled)

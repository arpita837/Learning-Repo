import pandas as pd

# Creating a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 22, 28],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Accessing columns
names = df['Name']
ages = df['Age']

# Adding a new column
df['Salary'] = [60000, 70000, 55000, 80000]

# Display the modified DataFrame
print(df)

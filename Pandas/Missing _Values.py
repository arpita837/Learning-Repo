import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, None, 22, 28],
        'City': ['New York', 'Los Angeles', None, 'Houston']}
df = pd.DataFrame(data)

# Handling missing values
df_cleaned = df.dropna()  # Remove rows with any missing value

print("Original DataFrame:")
print(df)

print("\nCleaned DataFrame:")
print(df_cleaned)

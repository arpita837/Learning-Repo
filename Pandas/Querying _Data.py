import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 22, 28],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df = pd.DataFrame(data)
young_people = df[df['Age'] < 30]
new_yorkers = df.query("City == 'New York'")

print("Young People:")
print(young_people)

print("\nNew Yorkers:")
print(new_yorkers)

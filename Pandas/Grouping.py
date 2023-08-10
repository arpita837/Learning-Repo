import pandas as pd

data = {'City': ['New York', 'Los Angeles', 'Chicago', 'New York', 'Chicago'],
        'Population': [8623000, 3990456, 2716000, 8623000, 2716000]}
df = pd.DataFrame(data)

city_stats = df.groupby('City')['Population'].agg(['sum', 'mean', 'count'])

print("City Statistics:")
print(city_stats)

import pandas as pd

data = pd.read_csv('data_ordered.csv')

d1 = data[['year', 'team_id', 'soa']]

sorted = pd.DataFrame.sort_values(d1, 'soa')
print(sorted)
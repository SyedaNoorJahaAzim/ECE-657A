import pandas as pd

df = pd.read_csv('wdbc.csv')
df.set_index('ID_number', inplace=True)

print('Description: ')
print(df.describe())

print('Mean: ')
print(df.mean(axis=0))

print('Mode: ')
print(df.mode(axis=0))

print('Skew: ')
print(df.skew(axis=0))

print('Standard Deviation: ')
print(df.std(axis=0))

print('Variance: ')
print(df.var(axis=0))
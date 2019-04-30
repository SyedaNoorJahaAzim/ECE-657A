import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('wdbc.csv')
df.set_index('ID_number', inplace=True)

data_M = df[df['Diagnosis'] == 'M'].median(axis=0)
data_B = df[df['Diagnosis'] == 'B'].median(axis=0)

plt.hist(data_M, bins=range(int(min(data_M)), int(max(data_M)) + 1, 1), label='M')
plt.hist(data_B, bins=range(int(min(data_B)), int(max(data_B)) + 1, 1), label='B')
plt.xlabel('Features')
plt.ylabel('Mean')
plt.legend(loc='upper right')
plt.show()
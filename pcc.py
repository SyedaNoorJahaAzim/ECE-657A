import pandas as pd
from scipy.stats import pearsonr

df = pd.read_csv('wdbc.csv')
df.set_index('ID_number', inplace=True)

corr, _ = pearsonr(df.area, df.perimeter)
print('Pearsons Correlation Coefficient of Area and Perimeter: %.3f' % corr)
print('The pearsonr() SciPy function is used to calculate the Pearson correlation coefficient between two data samples \n' 
'Area and Perimeter. The Pearsons Correlation Coefficient of Area and Perimeter is 0.987, which indicates a notable \n' 
'correlation between the Area and Perimeter of cell nucleus. Therefore, we can interpret the area of the cell nucleus is \n' 
'proportional to its perimeter.')

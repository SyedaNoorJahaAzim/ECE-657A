import pandas as pd
from pandas import DataFrame
from scipy.spatial.distance import cdist

df = pd.read_csv('/Users/s.n.azim/Downloads/winequality-red .csv').head(10)


def distance(dType):
    arr = [['Nearest', 'Farthest']]

    for i in range(0, 10):
        new_data = df.drop(df.index[i])
        dist = cdist(df.loc[[i]], new_data, metric=dType)
        arr.extend([[dist.min().round(2), dist.max().round(2)]])

    return arr


print(DataFrame(distance('cityblock')).to_csv('Manhattan_Distance .csv', index=True, header=None))
print(DataFrame(distance('euclidean')).to_csv('Euclidean_Ddistance .csv', index=True, header=None))
print(DataFrame(distance('cosine')).to_csv('Cosine_Distance .csv', index=True, header=None))

import pandas as pd

df = pd.read_csv('/Users/s.n.azim/Downloads/winequality-red .csv').head(10)

minMax = ((df - df.min())/(df.max() - df.min())).round(4)
print(pd.DataFrame(minMax).to_csv('MinMax .csv', index=True, header=True))

zScore = ((df - df.mean())/df.std()).round(4)
print(pd.DataFrame(zScore).to_csv('ZScore .csv', index=True, header=True))

meanNorm = ((df - df.mean())/(df.max() - df.min())).round(4)
print(pd.DataFrame(meanNorm).to_csv('MeanNorm .csv', index=True, header=True))

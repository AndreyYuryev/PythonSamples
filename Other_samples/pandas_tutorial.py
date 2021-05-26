import pandas as pd
import numpy as np

SeriesA = pd.Series([5, 4, 3, 2, 1])
print(SeriesA)

SeriesA = pd.Series([5, 4, 3, 2, 1], index=['a', 'b', 'c', 'd', 'e'])
print(SeriesA)

SeriesB = pd.Series([9, 8, 7, 6, 5], index=['a', 'b', 'c', 'd', 'f'])

dictA = {'SeriesA': SeriesA, 'SeriesB': SeriesB}
df = pd.DataFrame(dictA)
print(df)
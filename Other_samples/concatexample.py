import pandas as pd

series_a = pd.Series([1,2,3,4,5], name="Python Series 1", index=[1,2,3,4,5])
series_b = pd.Series([6,7,8,9,10], name="Python Series 2", index=[4,5,6,7,8])

print(series_a)
print(series_b)

new_series_1 = pd.concat([series_a, series_b], axis=0)
new_series_2 = pd.concat([series_a, series_b], axis=1)
print(new_series_1)
print(new_series_2)


with pd.ExcelWriter("test.xlsx") as writer:
    new_series_1.to_excel(writer)

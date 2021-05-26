import numpy as np
import pandas as pd
import os

excel_file = "Pandas_Workbook.xlsx"
df = pd.read_excel(excel_file, sheet_name='List1')
print(df)

print(df.head(2))
print(df.tail(2))
print(df.index)
print(df.columns)
print(df.dtypes)

print(df['Name'])
print(type(df['Name']))

names = df['Name']
print(names[1])

#label
print(df.at[0, "Name"])

df2 = pd.read_excel(excel_file, index_col="Name")
print(df2)
print(df2.at["Adam", "Occupation"])
print(df2.iat[1, 1])

print(df.loc[[0,2], "Age":"Occupation"])
print('test', df.loc[df["Identifier"]==True])
print(df.iloc[2:0:-1, [0,1]])
import pandas as pd
import os
import matplotlib.pyplot as plt

file_path = os.path.join('..', 'scratch08', 'mpg.csv')
df = pd.read_csv(file_path)
print(df.head())
print('shape:', df.shape)
print('dtypes:', df.dtypes)
print(df.describe())

displ = df['displ']
print(displ)
cty = df['cty']

# plt.scatter(displ, cty)
# plt.show()

print(df.loc[0:3])
print(df.iloc[0:3])

# 데이터프레임에서 여러개의 변수들을 선택
print(df[['displ', 'cty', 'hwy']])

print(df.loc[0:3, ['manufacturer', 'model', 'displ']])
print(df.iloc[0:3, 0:3])
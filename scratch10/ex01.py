"""
pandas groupby, aggregate, apply
"""
import pandas as pd
import numpy as np

np.random.seed(1205)
df = pd.DataFrame({
    'key1': ['a','a', 'b', 'b', 'a'],
    'one': ['one','two', 'one', 'two', 'one'],
    'data1': np.random.randint(0,10,5),
    'data2': np.random.randint(0,10,5)
})
print(df)

grouped1 = df.groupby('key1')
print(grouped1)   # DataFrameGroupBy 객체

cnt = grouped1['data1'].count()
print(type(cnt))
print(cnt)
print(cnt['a'], cnt['b'])

print(grouped1['data1'].mean())

print(grouped1.mean())
print(grouped1.count())

grouped2 = df.groupby('one')
print(grouped2.mean())

grouped3 = df.groupby(['key1', 'one'])
print(grouped3['data1'].count())
print(grouped3.count())
print(grouped3.mean())

people = pd.DataFrame(np.random.randint(0,10,(5,5)),
                      columns=['a','b','c','d','e'],
                      index=['joe', 'steve', 'wes', 'jimmy', 'travis'])
print(people)

print(people.groupby(len).sum())
print(people.groupby(lambda x: x.startswith('j')).sum())
























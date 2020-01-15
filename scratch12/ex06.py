# Iterable : for-in 구문에서 사용할 수 있는 타입들
#  -> list, tuple, set, dict, numpy.ndarray, pandas.dataframe,...
#   for x in Iterable: ...

a = [1,3,0,9,-1]
result = sorted(a, key=lambda x: -abs(x))
print(f'a={a}, result={result}')
a.sort(key=lambda x: -abs(x))
print(f'a={a}, result={result}')

b = ['cat', 'bb', 'dogs', 'apple']
result = sorted(b, key=lambda x: len(x))
print(f'b={b}, result={result}')

c = {'cat':1, 'bb':-1, 'dogs':3, 'apple':5}
result = sorted(c, key=lambda x : len(x))
print(f'c={c}, result={result}')

result = sorted(c.values(), key=lambda x : abs(x))
print(f'c={c}, result={result}')

key, val = sorted(c.items(), key=lambda x:x[1], reverse=True)[0]
print(f'c={c}, key={key}, val={val}')

max = max(c.items(), key=lambda x:x[1])
print(max)
print('========================================================================')


class person:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person(이름: {self.name}, 나이: {self.age})'


p1 = person('이지수', 10)
p2 = person('심진섭', 20)
p3 = person('조성우', 30)

persons = [p1,p2,p3]
result = sorted(persons, key=lambda x:x.name)
print(f'persons:{persons}, \nresult:{result}')

result = sorted(persons, key=lambda x:x.age)
print(f'persons:{persons}, \nresult:{result}')

# field, property, member variable --> 다 동일한 의미   :  class가 가지고 있는 변수들
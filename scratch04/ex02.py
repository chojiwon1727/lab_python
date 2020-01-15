"""
numpy 패키지를 사용한 벡터 연산
"""
import math

import numpy as np

print('numpy version:', np.__version__)

# 파이썬 list 데이터 타입의 연산
v = [1,2]  # class list
print('v=',type(v))
w = [2,3]
print('w=',type(w))
print(v+w)
# print(v-w)


# numpy 패키지의 ndarray타입을 사용
v = np.array([1,[1,2],[3,4]])
print(type(v))
print(v.ndim)
print(v.shape)

v = np.array([
    [1,2],
    [3,4]
])
print(v.ndim)
print(v.shape)

v = np.array([1,2])
w = np.array([3,4])
vector_add = v + w
print(vector_add)
vector_sub = v - w
print(vector_sub)

vectors = np.array([
    [1,2],
    [3,4],
    [5,6]
])

np_sum = np.sum(vectors)
print(np_sum)

np_sum_by_col = np.sum(vectors, axis=1)
print(np_sum_by_col)

np_mean = np.mean(vectors)
print(np_mean)
np_mean_by_col = np.mean(vectors, axis=0)
print(np_mean_by_col)
np_mean_by_row = np.mean(vectors, axis=1)
print(np_mean_by_row)

v= np.array([1,2,3])
scalar_mul = 3*v
print(scalar_mul)

scalar_div = v/3
print(scalar_div)

v = np.array([1,2])
w = np.array([3,4])
print('dot = ', v.dot(w))


def norm(v):
    return math.sqrt(v.dot(v))

print(norm(w))

def dist(x,y):
    return norm(x-y)

print(dist(v,w))














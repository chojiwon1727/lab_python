import numpy as np

# numpy.c_와 numpy.r_의 비교

a = np.array([1,2,3])
print(a, type(a), a.shape)

b = np.array([4,5,6])
print(b, type(b), b.shape)

c = np.c_[a, b]
print(c, type(c), c.shape)    # a, b의 row의 개수가 같으면 됨     -> row 방향으로 합치기    -> column을 추가

d = np.r_[a, b]
print(d, type(d), d.shape)    # a, b의 column의 개수가 같으면 됨       -> column 방향으로 합치기  -> row를 추가

e = np.array([[1,2,3],
              [4,5,6]])

f = np.array([[10,20],
              [30,40]])

print(np.c_[e,f])
# print(np.r_[e,f])    # -> column의 개수가 다르기 때문에 불가능

print()
A = np.ones((2,3), dtype=np.int)
print(A)

B = np.zeros((2,3))
print(B)

C = np.arange(1, 7).reshape(3,2)
print(C)

D = np.random.random((3,3))
print(D)
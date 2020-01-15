import numpy as np

# numpy.ndarray 타입의 객체 생성
A = np.array([
    [1,2,3],
    [4,5,6]
])

B = np.array([
    [1,2],
    [3,4],
    [5,6]
])
print(A)

print(A.shape)
print(B.shape)

nrows, ncols = B.shape
print(nrows, 'x', ncols)

print(A[0,0])
print(A[0, 0:2])
print(B[:,0:1])

identity_matrix = np.identity(3)
print(identity_matrix)

print(A.transpose())

print(A.dot(B))
print(B.dot(A))
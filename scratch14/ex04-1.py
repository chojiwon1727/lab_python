import numpy as np


# 1. add(x, y)함수 만들기
def add(x, y):
    length = len(x)
    z = []
    row = 0
    for row in range(length):
        for col in range(length-1):
            col = 0
            a = x[row][col] + y[row][col]
            col += 1
            b = x[row][col] + y[row][col]
            z.append([a,b])
        row += 1
    return z


# 2. subtract(x, y)함수 만들기
def subtract(x, y):
    length = len(x)
    z = []
    row = 0
    for row in range(length):
        for col in range(length - 1):
            col = 0
            a = x[row][col] - y[row][col]
            col += 1
            b = x[row][col] - y[row][col]
            z.append([a, b])
        row += 1
    return z


# 3. multiply(x, y)함수 만들기
def multiply(x, y):
    length = len(x)
    z = []
    row = 0
    for row in range(length):
        for col in range(length - 1):
            col = 0
            a = x[row][col] * y[row][col]
            col += 1
            b = x[row][col] * y[row][col]
            z.append([a, b])
        row += 1
    return z


# 4. divide(x, y)함수 만들기
def divide(x, y):
    length = len(x)
    z = []
    row = 0
    for row in range(length):
        for col in range(length - 1):
            col = 0
            a = round(x[row][col] / y[row][col], 3)
            col += 1
            b = round(x[row][col] / y[row][col], 3)
            z.append([a, b])
        row += 1
    return z


# 5. dot(x,y)함수 만들기
# def dot(x, y):
#     z = []
#     sum = 0
#     for x_i, y_i in zip(x,y):
#        sum += x_i*y_i
#        z.append(sum)
#     return z

def my_dot(x, y):
    """
    두 행렬 x, y의 dot연산 결과 리턴
    dot_ik = sum(j)[x_ij * y_jk]

    *x와 y는 ndarray인 경우에만 사용 가능*
    """
    if x.shape[1] != y.shape[1]:
        raise ValueError('x의 column과 y의 row개수는 같아야 합니다.')

    n_row = x.shape[0]   # dot 결과 행렬의 row 개수
    n_col = y.shape[1]   # dot 결과 행렬의 column 개수
    temp = x.shape[1]    # 각 원소들끼리 곱한 결과를 더하는 횟수
    numbers = []
    for i in range(n_row):
        for k in range(n_col):
            n = 0
            for j in range(temp):
                n += x[i,j] * y[i,j]     # dot 결과 행렬의  [i, j]번째 원소의 값 계산
            numbers.append(n)            # [i, j]번째 원소를 리스트에 추가
    return np.array(numbers).reshape(n_row, n_col)    # 결과를 (n_row, n_col)모양의 행렬로 변환해서 리턴


def my_dot2(x, y):
    """
    두 행렬 x, y의 dot연산 결과 리턴
    dot_ik = sum(j)[x_ij * y_jk]

    *x와 y는 ndarray인 경우에만 사용 가능*
    """
    if x.shape[1] != y.shape[1]:
        raise ValueError('x의 column과 y의 row개수는 같아야 합니다.')

    n_row = x.shape[0]   # dot 결과 행렬의 row 개수
    n_col = y.shape[1]   # dot 결과 행렬의 column 개수
    temp = x.shape[1]    # 각 원소들끼리 곱한 결과를 더하는 횟수
    numbers = np.zeros((n_row, n_col))
    for i in range(n_row):
        for k in range(n_col):
            n = 0
            for j in range(temp):
                n += x[i,j] * y[i,j]
            numbers[i,k] = n
    return numbers

if __name__ == '__main__':
    x = [[1,2],
         [3,4]]

    y = [[5,6],
         [7,8]]

    print(add(x, y))
    print(subtract(x, y))
    print(multiply(x, y))
    print(divide(x, y))
    # print(my_dot(x, y))

    # inverse = np.linalg.inv(x)
    # print(inverse)

    # transpose = np.ndarray.transpose()
    # print(transpose)
























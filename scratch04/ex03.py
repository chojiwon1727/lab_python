def shape(matrix):
    """
    행렬의 행과 열의 개수를 tuple형태로 리턴하는 함수
    :param matrix: 행렬(행의 개수가 n개이고, 열의 개수가 m개인 2차원 리스트)
    :return: tuple (n,m)
    """

    n = len(matrix)
    m = len(matrix[0])
    return n, m

def get_row(matrix, index):
    """
    주어진 행렬(matrix)에서 index에 해당하는 row를 리턴하는 함수

    :param matrix: n x m 행렬
    :param index: 행번호(0시작)
    :return: 벡터(원소가 m개인 1차원 리스트)
    """
    return matrix[index]



def get_col(matrix, index):
    """
    주어진 행렬에서 index에 해당하는 column을 리턴하는 함수
    :param matrix: n x m 행렬
    :param index: 행번호(0시작)
    :return: 벡터(원소가 n개인 1차원 리스트)
    """
    # result = []
    # for x in matrix:
    #     result.append(x[index])
    # return result
    return [x[index] for x in matrix]

def make_matrix(nrows, ncols, fn):
    """
    함수(fn)의 리턴값들로 이뤄진 nrows x ncols 행렬을 생성

    :param nrows: 행의 개수
    :param ncols: 열의 개수
    :param fn: 함수(fn(nrows,ncols) = scalar)
    :return: nrows x ncols 행렬
    """
    matrix = []                   # 빈 리스트 생성 -> 2차원 리스트
    for i in range(nrows):        # 행의 개수만큼 반복
        row = []                  # 빈 리스트 생성 -> 행렬에 추가될 행(1차원 리스트)
        for j in range(ncols):
            row.append(fn(i,j))   # row에 아이템 추가
        matrix.append(row)        # 행렬에 row추가
    return matrix


def transpose(matrix):
    """
    주어진 행렬에서 행과 열을 뒤바꾼 행렬(전치행렬)

    :param matrix: n x m 행렬
    :return: m x n 행렬
    """
    nrows, ncols = shape(matrix)
    t = make_matrix(ncols, nrows, lambda x,y: matrix[y][x])
    return t


def transpose(matrix):
    nrows = len(matrix)
    ncols = len(matrix[0])
    # t = []
    # for j in range(ncols):
    #     t.append(get_col(matrix, j))
    # return t
    return [get_col(matrix, j) for j in range(ncols)]


def transpose(matrix):
    nrows = len(matrix)
    ncols = len(matrix[0])
    # t = []
    # for j in range(ncols):
    #     t_row = []     #전치 행렬의 행(row)
    #     for i in range(nrows):
    #         t_row.append(matrix[i][j])
    #     t.append(t_row)
    # return t
    return [[matrix[i][j] for i in range(nrows)] for j in range(ncols)]


def transpose(matrix):
    print('unpacking 연산자 *를 사용한 transpose')
    t = []
    for col in zip(*matrix):
        t.append(list(col))
    return t


if __name__=='__main__':
    #  2 x 3 행렬(row = 2, column = 3)
    A = [
        [1,2,3],
        [4,5,6]
    ]

    #  3 x 2 행렬(row = 3, column = 2)
    B = [
        [1,2],
        [3,4],
        [5,6]
    ]

    print(A)
    print(B)

    print('shape A:', shape(A))
    print('shape B:', shape(B))

    print('get_row:', get_row(A, 1))
    print('get_col:', get_col(A, 1))

    m = make_matrix(3,2, lambda x,y: x+y)
    print(m)

    def identity(x,y):
        if x == y:
            return 1
        else:
            return 0

    print('At=',transpose(A))
    print('Bt=',transpose(B))


a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
for x,y,z in zip(a,b,c):
    print('zip:', x, y, z)

print('A=', A)
print('*A=', *A)
print('B=', B)
print('*B=', *B)

for x, y in zip(*A):
    print(x,y)
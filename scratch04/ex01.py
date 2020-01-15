import math
def add(v, w):
    """
    주어진 두개의 n차원 벡터에서 성분별로 더하기를 해서
    새로운 n차원의 벡터를 리턴하는 함수

    :param v: n차원 벡터(성분이 n개인 벡터)
    :param w: n차원 벡터(성분이 n개인 벡터)
    :return: 각 성분별로 더하기 결과를 갖는 벡터
    """
    result = [v_n + w_n for v_n, w_n in zip(v, w)]
    if len(v) != len(w):
        raise ValueError('v와 w는 같은 차원의 벡터여야 합니다')
    return result


def subtract(v, w):
    """
    주어진 두개의 n차원 벡터에서 성분별로 빼기를 해서
    새로운 n차원의 벡터를 리턴하는 함수

    :param v: n차원의 벡터(성분이 n개인 벡터)
    :param w: n차원의 벡터(성분이 n개인 벡터)
    :return: 각 성분별로 빼기 한 결과를 갖는 벡터
    """
    if len(v) != len(w):
        raise ValueError('v와 w는 같은 차원의 벡터여야 합니다')
    return[v_n - w_n for v_n, w_n in zip(v, w)]

def vector_sum(vectors):
    """
    모든 벡터들에서 각 성분별 더하기 수행
    vector_sum([[1,1],[3,4],[5,6],[7,8]]) --> [16,19]

    :param vectors: n차원 벡터들의 리스트(2차원 리스트)
    :return: n차원 벡터
    """

    num = len(vectors[0])
    for vector in vectors[1:]:
        if num != len(vector):
            raise ValueError('벡터의 길이는 같아야 합니다')

    # result = [0 for _ in range(num)]
    # for i in range(num):
    #     for vector in vectors:
    #         result[i] += vector[i]
    # return result


    result2 = vectors[0]
    for vector in vectors[1:]:
        result2 = add(result2, vector)
    return result2


def scalar_multiply(c, vector):
    """
    c * [x1, x2, x3, ...] = [cx1, cx2, cx3, ...]
    :param c: 숫자(스칼라, scalar)
    :param vector: n차원 벡터(n개의 아이템을 갖는 1차원 리스트)
    :return: n차원 벡터
    """
    return [c * v_i for v_i in vector]


def dot(x,y):
    """
    [v1, v2, v3, ...] @ [w1, w2, w3, ...] = v1w1+v2w2+v3w3 + ... = scalar
    :param x: n차원 벡터
    :param y: n차원 벡터
    :return: 숫자(스칼라, scalar)
    """

    if len(x) != len(y):
        raise ValueError('벡터의 길이는 같아야 합니다!')

    sum1 = 0
    for x_i, y_i in zip(x,y):
        sum1 += x_i*y_i
    return sum1


def vector_mean(vectors):
    """
    주어진 벡터들의 리스트에서 각 항목별 평균으로 이루어진 벡터 리턴

    :param vectors: n차원 벡터들의 리스트
    (길이가 n인 1차원 리스트를 아이템으로 갖는 2차원 리스트)
    :return: n차원 벡터
    """
    num = len(vectors[0])
    for i in vectors[1:]:
        if num != len(i):
            raise ValueError('벡터들의 길이는 같아야 합니다!')

    length = len(vectors)
    return scalar_multiply(1/length, vector_sum(vectors))

def sum_of_squares(vector):
    """
    vector = [x1, x2, x3, ...xn]일 때, x1**2 + x2**2 +.... + xn**2리턴
    :param vector: n차원 벡터
    :return: 숫자
    """
    sum1=0
    for i in vector:
        sum1 += i**2
    return sum1


def magnitude(vector):
    """
    벡터의 크기를 리턴하는 함수 - math.sqrt(sum_of_squares)
    :param vector:
    :return:
    """
    return math.sqrt(sum_of_squares(vector))


def squared_distance(v,w):
    """
    (v1-w1)**2 + (v2-w2)**2 + ... + (vn-wn)**2
    :param v: n차원 벡터
    :param w: n차원 벡터
    :return: 숫자
    """
    sum1 = 0
    for v_i, w_i in zip(v, w):
        sum1 += (v_i - w_i)**2
    return sum1


def distance(v,w):
    """
    두 벡터 v와 w사이의 거리를 리턴하는 함수 - sqrt(squared_distance)

    :param v: n차원 벡터
    :param w: n차원 벡터
    :return: 숫자
    """
    return math.sqrt(squared_distance(v,w))


if __name__ == '__main__':
    add1 = add([1,2,3,4], [10,7,9,5])
    print(add1)

    subtract1 = subtract([10,9,2], [1,2,3])
    print(subtract1)

    a = [1,2,3]
    b = [5,6,7]
    c = [8,9,10]
    vector = [a,b,c]
    vector_sum1 = vector_sum(vector)
    print(vector_sum1)

    scalar1 = scalar_multiply(3, a)
    print(scalar1)

    dot1 = dot(a, b)
    print(dot1)

    mean1 = vector_mean(vector)
    print(mean1)

    sumsqu = sum_of_squares(a)
    print(sumsqu)

    sumsqu2 = magnitude(a)
    print(sumsqu2)

    sdist = squared_distance(a,b)
    print(sdist)

    dist = distance(a,b)
    print(dist)






























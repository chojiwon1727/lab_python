def n_sum(n):
    """
    1부터 n까지 숫자들의 합을 리턴하는 함수
    :param n:
    :return:
    """

    result = 0
    for i in range(n+1):
        result += i
        if i == n:
            break
    return result

print(n_sum(10))

def pow_n_sum(n):
    """
    1부터 n까지 숫자들의 제곱합을 리턴하는 함수
    :param n:
    :return:
    """

    result = 0
    for i in range(n+1):
        result += pow(i, 2)
        if i == n:
            break
    return result

print(pow_n_sum(3))

def find_max(numbers):
    """
    숫자들의 리스트를 전달받아서 최대값을 리턴하는 함수
    :param n:
    :return:
    """
    v_max = numbers[0]
    for i in numbers:
        if v_max < i:
            v_max = i
    return v_max

numbers = [10,20,30,40,50,60,70]
print(find_max(numbers))

def find_max_index(numbers):
    """
    숫자들의 리스트를 전달받아서 최대값의 인덱스를 리턴하는 함수
    :param n:
    :return:
    """
    v_max = numbers[0]
    for i in numbers:
        if v_max < i:
            v_max = i
    x = numbers.index(v_max)
    return x

numbers = [10,20,30,40,50,60,70]
print(find_max_index(numbers))
print()

def find_median(numbers):
    """
    숫자들의 리스트를 전달받아서 중앙값을 리턴하는 함수

    :param numbers:
    :return:
    """
    numbers.reverse()
    if len(numbers) % 2 == 1:     # 홀수
        x = len(numbers) / 2
        result = numbers.index(x)
    elif len(numbers) % 2 == 0:   # 짝수
        x = len(numbers) / 2

    return

# 12345    3    len = 5
# 123456   3.5  len = 6

numbers = [10,20,30,40,50,60,70]
print(find_median(numbers))
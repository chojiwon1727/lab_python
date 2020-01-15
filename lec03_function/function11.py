"""
람다 표현식(lambda expression) :
함수의 이름 없이 함수의 매개변수 선언과 리턴값으로만 표현하는 방법
"""

multiplication = lambda x, y: x * y
result = multiplication(11,11)
print(result)

division = lambda x,y : x/y
result = division(10,2)
print(result)


def calc(x,y,op):
    return op(x,y)

result = calc(1,2,lambda x,y: x+y)
print(result)
result = calc(1,2,lambda x,y: x/y)
print(result)

# 람다 표현식을 사용한 함수 예시
def my_filter(values, func):
    """
    리스트에 있는 원소들 중에서 필터링 조건(func)을 만족하는 원소들만으로 이루어진
    새로운 리스트를 출력하는 함수

    :param values: 리스트
    :param func: True, False를 리턴하는 함수수
   :return: 필터링된 새로운 리스트
    """
    result = []
    for item in values:           # 리스트의 모든 원소들에 대해서 반복
        if func(item):            # 필터링 조건 함수 func의 리턴 값을 검사
            result.append(item)   # 조건이 True인 경우에만 리스트에 추가
    return result


numbers = [1,-2,3,-4,-5,6,-7,8]
positive = my_filter(numbers, lambda x : x > 0)
print(positive)

evens = my_filter(numbers, lambda x: x%2 == 0)
print(evens)


lang = ['python', 'r', 'pl/sql', 'java', 'c/c++']
more_than_5 = my_filter(lang, lambda x:len(x)>5)
print(more_than_5)

def my_filter2(values, func):
    return [item for item in values if func(item)]

print(my_filter2(numbers, lambda x: x>0))


def my_mapper(values, func):
    """
    리스트의 item들을 함수의 파라미터에 전달해서,
    리스트의 아이템을 key, 함수의 리턴 값을 value로 하는
    dict를 리턴

    :param values: 리스트
    :param func: 파라미터가 1개인 함수수
   :return: dict
    """
    result = {}
    for item in values:
        # dict의 키는 item, dict의 값(value)는 함수 func의 리턴값
       result[item] = func(item)
    return result

result = my_mapper(lang, lambda x: len(x))
print(result)

def my_mapper2(values, func):
    return{k:func(k) for k in values}
print(my_mapper2(lang, lambda x:len(x)))


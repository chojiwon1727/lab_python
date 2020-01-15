"""
def 함수이름(파라미터 : 타입, 파라미터2 : 타입, ...) -> 리턴타입:
    함수기능
"""

def subtract(x:int, y:int) -> int:
    return x-y

result = subtract(1,2)
print(result)

def my_sum(numbers:list)->float:
    """
    숫자들(int, float)들이 저장된 리스트를 전달받아서,
    모든 원소들의 합을 리턴하는 함수

    :param numbers: 숫자들이 저장된 리스트
    :return: 리스트의 모든 원소들의 합
    """
    result = 0
    for i in numbers:
        result += i
    return result



numbers = [1.1,2.2,3.3,4.4,5.5]

result = my_sum(numbers)
print(result)



def my_mean(numbers : list) -> float:
    """
    숫자들을 저장하는 리스트를 전달받아서,
    모든 원소들의 평균을 계산해서 리턴

    :param numbers: 숫자들이 저장된 리스트
    :return: 리스트의 모든 원소들의 평균
    """
    result = 0
    for i in numbers:
        result += i

    my_mean = result / len(numbers)

    return my_mean

# return my_sum(numbers) / len(numbers)

numbers2 = [1,2,3,4,5]

result = my_mean(numbers2)
print(result)


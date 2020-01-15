import numpy as np
def fn_vararg(*varargs):
    print(varargs)
    print(*varargs)
    for arg in varargs:
        print(arg)

fn_vararg(1, 2, 3, 4)
print('-------')

def summation(*args):
    """
    임의의 개수의 숫자들을 전달받아서 그 숫자들의 총합을 리턴하는 함수

    :param args: 총합을 계산할 숫자들
    :return: 숫자들의 합
    """
    result = 0
    for n in args:
        result += n
    return result

print(summation(1,2,3,4,5))

def fn_vararg2(a, *b):
    print(f'a={a}')
    print(f'b={b}')

fn_vararg2(1)

def fn_vararg3(*a, b):
    print(f'a={a}')
    print(f'b={b}')

fn_vararg3(b=2)
print()


def calculator(*values, operator):
    """
    operator가 '+'인 경우에는 values들의 합계를 리턴하고
    operator가 '*'인 경우에는 values들의 전체 곱을 리턴하는 함수

    :param values:
    :param operator:
    :return:
    """
    if operator == '+':
        result = 0
        for n in values:
            result += n
        return result
    elif operator == '*':
        result2 = 1
        for n in values:
            result2 *= n
        return result2

print(calculator(10,20,30, operator='+'))
print(calculator(10,20,30, operator='*'))
print(calculator(10,20,30, operator='-'))



















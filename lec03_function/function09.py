"""
재귀 함수(recursive function)
"""


# factorial
# 0! = 1    --> 재귀함수가 끝나서 마지막으로 출력될 값을 지정해줘야 함
# n! = 1 x 2 x 3 x ... x (n-1) x n = (n-1)! x n
def factorial1(n: int) -> int:
    result = 1
    for x in range(1, n + 1):
        result *= x  # result = result * n
    return result


def factorial2(n: int) -> int:
    if n == 0:
        return 1
    elif n > 0:
        return factorial2(n - 1) * n


for x in range(6):
    print(f'{x}! = {factorial2(x)}')

print('--------------------')


# 재귀함수를 사용한 하노이탑

def hanoi_tower(n, start, target, aux):
    """
    재귀함수를 사용해서 하노이 탑 문제 해결 방법 출력

    :param n: 옮길 원반의 수(양의 정수)
    :param start: 원반들이 있는 시작 기둥 번호
    :param target: 원반들을 모두 옮겨 놓을 타겟 기둥 번호
    :param aux: 보조 기둥으로 사용할 기둥 번호
    :return: None
    """
    if n == 1:
        print(f'{start} -> {target}')
        return  # 함수 종료의 의미

    # n-1개의 원반을 aux 기둥으로 모두 옮김(이 과정에서는 aux가 target이 되고 targe이 aux가 됨)
    hanoi_tower(n - 1, start, aux, target)
    # 시작 기둥에 남아 있는 한개의 원반을 목표 기둥으로 옮김
    print(f'{start} -> {target}')
    # aux기둥에 남아 있는 (n-1)개의 원반을 start 기둥을 aux로 사용해서 target으로 옮김
    hanoi_tower(n - 1, aux, target, start)

    # 원반 1~4개짜리 하노이탑
    for n in range(1, 5):
        print('하노이탑 n=', n)
        hanoi_tower(n, start=1, target=3, aux=2)
        print('==============================')

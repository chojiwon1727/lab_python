# 함수 정의
def test(x,y):
    print(f'x = {x}, y={y}')
    return x+y, x-y

# 함수 호출
# test()    --> 실행 중에 TypeError 발생(파라미터 타입은 검사하지 않지만 파라미터 개수는 검사함)
# keyword argument : 함수를 호출할 때, argument를 파라미터 = 값 형식으로 전달하는 방식

plus, minus = test(x=20, y=10)
print(minus)
plus, minus = test(y=20, x=10)
print(minus)


def show_msg(msg : str = 'Hello', times : int = 1) -> None:
    print(msg*times)

show_msg('졸리세요?', 5)
show_msg('네.. 많이 졸려요..')
show_msg()
print()

# def test2(x=1, y):
#     return x + y


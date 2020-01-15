import numpy as np

def user_input():
    """
    사용자에게 1,2,3 중 하나의 숫자를 입력하도록 안내하고
    사용자가 입력한 숫자를 리턴
    (사용자가 숫자로 변환할 수 없는 문자를 입력하면, 안내문 출력 후 다시 입력받음)
    (사용자가 1,2,3 이외의 숫자를 입력한 경우, 안내문 출력 후 다시 입력받음)

    :return: 1,2,3 중 하나
    """
while True:
    try:
        user = int(input('1,2,3 중에 숫자 하나 입력>>'))
        if(user != 1 and user != 2 and user != 3):
            raise ValueError('1,2,3 이외의 숫자는 입력할 수 없습니다!')
        computer = np.random.randint(1, 4)
        # print('computer:', computer)
        # print('user:', user)
        if user == 1:
            if user == computer:
                print('비김')
            elif user < computer:
                print('내가 짐')
            else:
                print('내가 이김')
        elif user == 2:
            if user == computer:
                print('비김')
            elif user < computer:
                print('내가 짐')
            else:
                print('내가 이김')
        else:
            if user == computer:
                print('비김')
            elif computer == 1:
                print('내가 짐')
            else:
                print('내가 이김')
        break
    except ValueError as e:
        print(e.args)



user = user_input()
print('입력 값 =', user)
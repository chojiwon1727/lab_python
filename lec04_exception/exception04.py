"""
사용자 정의 오류 발생
"""

while True:
    try:
        age = int(input('나이를 입력하세요>>'))
        if(age<0):
            raise ValueError('나이는 0 또는 양의 정수여야 합니다')
        print('입력한 나이:', age)
        break
    except ValueError as e:
        print(e.args)

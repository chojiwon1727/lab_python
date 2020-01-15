"""
여러가지 print()방법
"""

print('Hello, python!')

age = 16
name = '오쌤'
print('나이:', age, ', 이름:', name)
print(f'나이: {age}, 이름: {name}')    # formatted string
print('나이: {}, 이름: {}'. format(age, name))
print('나이: %d, 이름:%s' %(age, name))     # %d : 정수(digit). %f : 실수(floating-point number), %s : 문자열(string)

# 사용자 입력(키보드 입력) 처리
print('>>>이름을 입력하세요')
name = input()
print(f'name : {name}')

age = input('>>> 나이를 입력하세요')
print(f'age = {age}')

# print(age +1)  --> 불가능(age 변수에 저장된 값 16을 문자열로 취급하기 때문에 연산 불가)
# Crrl + / : 주석 토글


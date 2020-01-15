# 번호, 이름, 수학점수, 과학점수, 컴퓨터점수
from collections import namedtuple
from typing import NamedTuple

student_1 = (1, '홍길동', 10, 20, 30)
print('번호 : ', student_1[0])
print('과학점수 : ', student_1[3])

# 튜플(tuple) 타입의 단점:
# 1) 해당 인덱스의 원소가 무슨 값을 의미하는지 파악하기가 어려움
# 2) 특정 원소에 접근(read, write)하기 위해서는 인덱스만 사용할 수 있음
stu_dect = {'no': 2, 'name': '김길동', 'math': 90, 'science': 50, 'cs': 100}
# --> 단점을 극복한 것 : dict   --> but, dict는 값을 변경할 수 있음
# --> dict 처럼 사용하되, 값을 변경할 수 없는 타입이 namedtuple

Student = namedtuple('Student', ('no', 'name', 'math', 'science', 'cs'))
student_2 = Student(3, '허균', 100, 100, 100)
print(student_2)
print(f'번호 : {student_2[0]}, {student_2.no}')


# Python 3.6부터 NamedTuple을 class처럼 선언하는 방식이 생김
class Student2(NamedTuple):      # Student2 class는 NamedTuple class를 상속받는다!
    # field 선언 - 변수 타입 annotation을 반드시 추가해야 함
    no: int
    name: str
    math: int
    science: int
    cs: int


student_3 = Student2(4, 'abc', 90, 88, 77)
print(student_3)

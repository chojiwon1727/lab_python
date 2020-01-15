"""
파이썬 데이터 타입 :
1. 숫자타입 : int(정수), float(실수), complex(복소수)
2. 논리타입 : bool  <-- 단순히 T,F를 저장하는 데이터 타입
3. 문자타입 : str
4. 시퀀스(sequence) : list, tuple
5. 매핑(mapping) : dict
6. 집합 : set  <- 중복된 값 저장 불가
7. None : 값이 없음을 나타내는 데이터 타입   <- 데이터를 저장하는 메모리의 주소가 없음
"""

# 1. 숫자타입
intval = 123
print(type(intval)) # 변수의 타입 확인
print(id(intval)) # 123이라는 숫자가 저장되어 있는 메모리의 주소 출력

flaotval = 3.123456
print(type(flaotval))

complexval = 1 + 2j
print(type(complexval))

print(1j ** 2)

# 2. 논리타입
result = 10 < 2
print(result)
print(type(result))

# 3. 문자타입
intval = 123
print(type(intval))

# 7. None
name = None
print(type(name))
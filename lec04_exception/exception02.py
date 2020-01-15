
try:
    numbers = [1,2,3]
    for i in range(1,4):
        print(i, ':', numbers[i])
except ValueError:
    print('값 에러 발생')
except IndexError:
    print('인덱스 에러 발생')
else:
    print('try의 모든 내용을 정상적으로 실행')
finally:
    print('finally 블록')


# 파일 열기
f = open('test.txt', mode='w', encoding='UTF-8')

# 파일 쓰기
for i in range(1,11):
    f.write(f'{i}번째 줄 \n')

# 파일 닫기
f.close()


with open('test2.txt', mode='w', encoding='utf-8') as f:
    f.write('Hello, Python\n')
    f.write('점심식사는 맛있게 하셨나요?\n')
    f.write('0123456789\n')
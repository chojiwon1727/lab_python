import csv

# 문자열(string)을 아이템으로 갖는 리스트
row1 = ['test1', 'success', 'Mon']
row2 = ['test2', 'failure, kind of', 'Tue']
row3 = ['test3', 'success, kind of', 'Wed']
result = [row1, row2, row3]
print(result)

# 파일을 쓰기모드로 열기
with open('test_result.csv', mode='w', encoding='UTF-8', newline= '') as f:
    writer = csv.writer(f, delimiter=',')
    for row in result:
        writer.writerow(row)

print('\ncsv 모듈을 사용하지 않을 경우')
# csv모듈을 사용하지 않고 csv파일을 읽었을 때 문제점
with open('test_result.csv', mode='r', encoding='UTF-8') as f:
    for line in f:
        print(line.strip().split(','))

print('\ncsv 모듈을 사용하는 경우')
with open('test_result.csv', mode='r', encoding='UTF-8')as f:
    reader = csv.reader(f) # csv모듈의 reader객체를 생성
    for row in reader:
        print(row)



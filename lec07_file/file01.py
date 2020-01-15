"""
os 모듈의 변수와 함수들
"""
import os

# CWD: Current Working Directory(현재 작업 디렉토리/폴더)
print(os.getcwd())

print(os.name)

if os.name == 'nt':   # windows os인 경우
    file_path = '.\\temp\\temp.txt'
else:                 # windows os가 아닌 경우
    file_path = './temp/temp.txt'

print(file_path)

file_path = os.path.join('.', 'temp', 'temp.txt')
print(file_path)

print(os.path.isdir('.'))
print(os.path.isdir('file01.py'))
print(os.path.isfile('.'))
print(os.path.isfile('file01.py'))

with os.scandir('.') as my_dir:
    for entry in my_dir:
        print(entry.name, '\t', entry.is_file())

# 파일(디렉토리) 이름 변경
try:
    os.rename('temp', 'test')
except FileNotFoundError:
    print('temp 폴더가 없음')

try:
    os.rmdir('test')
except FileNotFoundError:
    print('삭제 권한 없음')

try:
    os.mkdir('test2')
except FileExistsError:
    print('test2 폴더가 이미 있음')
# os.mkdir('test2\\temp')
# os.makedirs('test2\\temp')

# os.mkdir('test1\\temp')
# test1폴더가 없기 때문에 그 하위 폴더를 생성할 수 없음

try:
    os.makedirs('test1\\temp')
    print('test1\\temp 폴더 생성 성공')
except FileExistsError:
    print('test1\\temp 폴더가 이미 있음')
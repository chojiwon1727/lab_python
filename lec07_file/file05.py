"""
file open 모드(mode)
   r : read
   w : write
   a : append
"""
try:
    with open('NoFile.txt', mode='r') as f:
        pass
except FileNotFoundError:
    pass

with open('Newfile.txt', mode='w', encoding='utf-8') as f:
    f.write('test 테스트...')


with open('Newfile.txt', mode='w', encoding='utf-8') as f:
    pass

with open('Append.txt', mode='a', encoding='utf-8') as f:
    f.write('test \n')

with open('Append.txt', mode='a', encoding='utf-8') as f:
    f.write('추가...')
# open
f = open('test.txt', mode='r', encoding='utf-8')

# read : read(), readline()
# content = f.read()
content = f.read(2)
print(content)
# content = f.read(5)
# print(content)
# close
f.close()

f = open('test2.txt', mode='r', encoding='utf-8')

line = f.readline().strip()
print(f'line: {line}, length: {len(line)}')
line = f.readline().strip()
print(f'line: {line}, length: {len(line)}')

f.close()

f = open('test2.txt', mode='r' , encoding='utf-8')

while True:
    line = f.readline()
    if line == '':
        break
    print(line.strip())

f.close()

f = open('test.txt', mode='r', encoding='utf-8')

line = f.readline()
while line:
    print(line.strip())
    line = f.readline()

f.close()

with open('test2.txt', mode='r', encoding='utf-8') as f:
    line = f.readline()
    while line:
        print(line.strip())
        line = f.readline()

















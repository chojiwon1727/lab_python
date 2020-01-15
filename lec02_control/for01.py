for i in range(5):
    print(i, end = ' ')
print()

for i in range(1,5):
    print(i, end=' ')
print()

for i in range(1,5,2):
    print(i, end=' ')
print()

for s in 'Hello, Python!':
    print(s, end=' ')
print()

lang = ['pl/sql', 'r', 'python', 'java']
for l in lang:
    print(l, end=' ')
print()

for i in range(len(lang)):
    print(i, lang[i])
print()

alpha = {1:'a', 2:'b', 3:'c'}
print(alpha.keys())
for key in alpha.keys():
    print(key, alpha[key])
print()

for key in alpha:
    print(key)

for item in alpha.items():
    print(item)

for key, value in alpha.items():
    print(key, value)






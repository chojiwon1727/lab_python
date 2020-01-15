n = 3
if n % 2:
    print('홀수')
else:
    print('짝수')


my_list = ['R']
if my_list:
    print(my_list)
else:
    my_list.append('python')
    print(my_list)

lang = ['PL/SQL', 'R']
if 'python' in lang:
    pass
else:
    lang.append('python')
print(lang)

lang = ['PL/SQL', 'R']
if 'python' not in lang:
    lang.append('python')
print(lang)


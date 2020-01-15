fibo =[0,1]
for n in range(2,20):
    x = fibo[n-1] + fibo[n-2]
    fibo.append(x)
print(fibo)
print()




for n in range(2,11):
    isprime = True
    for divi in range(2,n):
        if n % divi == 0:
           print(f'{n} = {divi} x {n/divi}')
           isprime = False
           break
    if isprime:
        print(f'{n}은 소수입니다')
print()

for i in range(5):
    if i == 5:
        break
    print(i, end=' ')
else:
    print('모든 반복을 끝냄')
print()

for n in range(2,11):
    for d in range(2,n):
        if n % d == 0:
            break
    else:
        print(f'{n} : 소수')
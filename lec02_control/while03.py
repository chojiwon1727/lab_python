"""
반복문 연습
"""
v_sum = 0
for n in range(1,101):
    v_sum = v_sum + n
print(v_sum)

v_sum2 = [x for x in range(1,101)]
print(sum(v_sum2))

v_sum3, n = 0, 1
while n <=100:
    v_sum3 += n
    n += 1
print(v_sum3)


v_sum4 = 0
n = 1
while v_sum4 <= 100:
    v_sum4 += n
    print(f' n = {n} , sum = {v_sum4}')
    n += 1


for i in range(1,9):
    for v in range(1, i):
        print('T', end=' ')
    print()
print()


i = 1
while i < 9:
    v = 1
    while v < i:
        print('T', end=' ')
        v += 1
    i += 1
    print()

# for i in range(1,9):
#     for v in range(1,i):
#         print( ,'T')
#     print()
# print()



i = 1
while i < 9:
    v = 1
    while v < i:
        print()
        v += 1
    i += 1
    print()






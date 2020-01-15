person = {'name':'오쌤', 'age':16, 'height':170.5}
print(person)
print(type(person))

print(person['name'])
print(person.keys())
print(person.values())
print(person.items())

student = {1: '강다혜', 2:'김수인', 3:'김영광'}
print(student[1])

student[4] = '김재성'
print(student)

student[4] = '홍길동'
print(student)

student.pop(4)
print(student)


book = {
    'title':'파이썬 프로그래밍 교과서',
    'authors':['제니퍼', '폴', '제이슨'],
    'company':'길벗',
    'ISBN':97911
}

print(book)
print(book['authors'][0])
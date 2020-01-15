numbers = [1,2,3,4,5]
print(numbers)
print(numbers[0])
print(numbers[4])
print(numbers[0:3])

numbers[0] = 100
print(numbers)

numbers.append(6)
print(numbers)

numbers.extend([7,8,9])
print(numbers)

numbers.append([7,8,9])
print(numbers)

numbers.remove(100)
print(numbers)

del numbers[1]
print(numbers)

empty = []

person = ['오쌤', 16, 170.5, True]
print(person)
print(person[0], type(person[0]))
print(person[1], type(person[1]))

name, age, height, marriage = person
print(name, age, height, marriage)

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix)
print(matrix[0], type(matrix[0]))
print(matrix[0][0])
print(matrix[1][1])

print(matrix[0:2])

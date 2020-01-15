import csv
import os

file_path = os.path.join('..', 'scratch08', 'mpg.csv')
with open(file_path, mode='r', encoding='UTF-8') as f:
    reader = csv.reader(f)
    reader.__next__()
    df = [line for line in reader]
print(df[0:5])
print(df[0][0], df[0][1], df[0][2])

displ = [float(row[2]) for row in df]
print(displ)

with open(file_path, mode='r', encoding='UTF-8') as f:
    reader = csv.DictReader(f)
    df = [line for line in reader]
print(df[0:5])
print(df[0]['manufacturer'])
print(df[0]['model'])
print(df[0]['displ'])

displ = [float(row['displ']) for row in df]
print(displ)
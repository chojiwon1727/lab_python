import pandas as pd
import numpy as np

a = pd.Series([1,3,5,np.nan,6,8])
print(type(a))
print(a)

# Series에서 특정 index의 item 선택 :  Series[index]
print(a[0])          # float 타입
# index 연산자 안에서 범위 연산자(:)를 사용할 수도 있음
print(a[0:3])        # Series 타입
print(a[[0,2,4]])    # Series 타입

# dict 타입의 데이터에서 DataFrame 생성
df = pd.DataFrame({
    'no':[3, 13, 23],
    'name':['김영광', '이은지', '조유경'],
    'gender':['M', 'F', 'F']
})
print(df)
print()

students = pd.DataFrame([
    [4, '김재성', 'M'],
    [14, '이재경', 'M'],
    [24, '조지원', 'F']], columns = ['번호', '이름', '성별'])
# students.columns = ['번호', '이름', '성별']
print(students)
print()
print(students.iloc[0,0])       # 0번 row, 0번 column의 아이템
print(type(students.iloc[0,0]))       # 0번 row, 0번 column의 아이템
print(students.iloc[0,0:3])     # 0번 row, 0,1,2 column의 아이템
print(type(students.iloc[0,0:3]))
print(students.iloc[0:2, 0:2])
print(students.iloc[:, 1:3])
print(students.iloc[1:3, :])
print(students.iloc[1:3])

print(students[[False, True, False]])
condition = students['성별'] == 'M'
print(condition)
print(students[['이름', '성별']])
print(students[condition])

students.columns = ['no', 'name', 'gender']
stu_df = pd.concat([df, students])
print(stu_df)

stu_df2 = pd.concat([df, students], ignore_index=True)
print(stu_df2)

# print(stu_df2.sort_values('no'))
# print(stu_df2.sort_values('gender'))

cond1 = stu_df2['no'] % 2 == 1
print(cond1)
cond2 = stu_df2['gender'] == 'F'
print(cond2)
print(stu_df2[cond1 & cond2]['name'])
import pandas as pd
import os
import matplotlib.pyplot as plt

file_path = os.path.join('.', 'gapminder.tsv')
gapminder = pd.read_csv(file_path, sep='\t', encoding='UTF-8')

# 1) 행과 열의 개수를 확인하고 앞, 뒤 데이터 5개씩 확인하기
print('1) 행과 열의 개수를 확인하고 앞, 뒤 데이터 5개씩 확인하기')
print(gapminder.shape)
# nrows, ncols = gapminder.shape
# print(f'nrows: {nrows}, ncols: {ncols}')
print(gapminder.head(5))
print(gapminder.tail(5))
# -> 행 인덱스로도 출력 가능
# print(gapminder.iloc[0:5])
# print(gapminder.iloc[nrows-6:nrows-1])

# 2) 컬럼 이름 출력하기
print('\n2) 컬럼 이름 출력하기')
print(gapminder.columns)

# 3) 각 컬럼의 데이터 타입 출력하기
print('\n3) 각 컬럼의 데이터 타입 출력하기')
print(gapminder.dtypes)

# 4) 국가이름, 기대수명, gdp 컬럼만 출력
print('\n4) 국가이름, 기대수명, gdp 컬럼만 출력')
print(gapminder[['country', 'lifeExp', 'gdpPercap']])

# 5) row index가 0, 99, 999인 row 출력
print('\n5) row index가 0, 99, 999인 row 출력')
print(gapminder.iloc[[0,99,999]])

# 6) row label이 840~851인 row의 나라이름, 기대수명, gdp출력
print('\n6) row label이 840~851인 row의 나라이름, 기대수명, gdp출력')
print(gapminder.loc[840:851, ['country', 'lifeExp', 'gdpPercap']])

# 7) 연도별 기대 수명의 평균 출력
print('\n7) 연도별 기대 수명의 평균 출력')
grouped = gapminder.groupby('year').mean()
print(grouped['lifeExp'])

# 8) 연도별, 대륙별 기대수명의 평균 출력
print('\n8) 연도별, 대륙별 기대수명의 평균 출력')
grouped = gapminder.groupby(['year', 'continent']).mean()
print(grouped['lifeExp'])

# 9) 연도별 기대수명 그래프 그리기
lifeExp_by_year = gapminder.groupby('year')['lifeExp'].mean()
plt.plot(lifeExp_by_year)
plt.title('lifeExp by year')
plt.show()

# 10) 연도별 전세계 인구수를 그래프로 그리기
pop_by_year = gapminder.groupby('year')['pop'].sum()
print(pop_by_year)
plt.title('pop by year')
plt.plot(pop_by_year)
plt.show()
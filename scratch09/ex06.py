import pandas as pd
import os

print('\n==== gapminder.tsv파일 ====\n')
df = pd.read_csv('gapminder.tsv', sep='\t', encoding='UTF-8')
print(df.head())

# SQL : select* from DataFrame where column == '';
df_afg = df[df['country'] == 'Afghanistan']
print(df_afg)

df_Kor = df[df['country'] == 'Korea, Rep.']
print(df_Kor)
print(df_Kor[['country', 'pop', 'gdpPercap']])
# print(type(df_Kor))
# print(df[df['country'] == 'Korea, Rep.'][['country', 'pop', 'gdpPercap']])

print('\n==== mpg.csv파일 ====\n')
mpg_path = os.path.join('..', 'scratch08', 'mpg.csv')
mpg = pd.read_csv(mpg_path, encoding='UTF-8')
# print(mpg.head())
cty_mean = mpg['cty'].mean()
df_mpg = mpg[mpg['cty'] > cty_mean]
print(df_mpg[['model', 'displ', 'cty', 'hwy']])

import cx_Oracle
import pandas as pd
import csv


def get_column_names_of(table, cursor):
    sql = f"""select column_name 
            from user_tab_columns 
            where table_name = upper('{table}') 
            order by column_id"""

    cursor.execute(sql)
    table_columns = [name[0] for name in cursor]
    return table_columns


def select_all_from(table, cursor):
    sql1 = f"select * from {table}"
    cursor.execute(sql1)
    data = [row for row in cursor]
    column_name = get_column_names_of(table, cursor)
    df = pd.DataFrame(data)
    df.columns = column_name
    return df
    # data = cursor.fetchall() 하면 자동으로 리스트 만들어줌(for구문 사용할 필요 없음)


if __name__ == '__main__':
    # 오라클 데이터 베이스 서버와 접속
    dsn = cx_Oracle.makedsn('localhost', 1521, 'orcl')   # localhost대신 ip주소 쓰면 됨(192.168.20.6)
    with cx_Oracle.connect('scott', 'tiger', dsn) as connection:
        with connection.cursor() as cursor:
            emp_columns = get_column_names_of('emp', cursor)
            print(emp_columns)

            emp_df = select_all_from('emp', cursor)
            print(emp_df)

            dept_df = select_all_from('dept', cursor)
            print(dept_df)

            sal_grade_df = select_all_from('salgrade', cursor)
            print(sal_grade_df)

            # DataFrame에 새로운 컬럼 추가 : DataFrame['컬럼이름'] = list 혹은 pandas.series
            # emp.df에 salgrade컬럼 추가하기

            # grade = []
            # for i in emp_df['SAL']:
            #     for j in range(len(sal_grade_df)):
            #         if sal_grade_df.loc[j, 'LOSAL'] <= i <= sal_grade_df.loc[j, 'HISAL']:
            #             grade.append(sal_grade_df.loc[j, 'GRADE'])
            #             break
            # emp_df['SAL_GRADE'] = grade
            # print(emp_df)

            grade = []
            for i in emp_df['SAL']:
                for rowname, row in sal_grade_df.iterrows():
                    if row['LOSAL'] <= i <= row['HISAL']:
                        grade.append(row['GRADE'])
                        break
            emp_df['SAL_GRADE'] = grade
            print(emp_df)

    # SQL join - pandas.merge
    print('\n연습문제 1번')
    emp_dept_inner = pd.merge(emp_df, dept_df,  on='DEPTNO')
    print(emp_dept_inner)

    emp_dept_left = pd.merge(emp_df, dept_df, how='left', on='DEPTNO')
    print(emp_dept_left)

    emp_dept_right = pd.merge(emp_df, dept_df, how='right', on='DEPTNO')
    print(emp_dept_right)

    # 연습문제
    print('\n 연습문제 2번')
    mgr_empno_inner = pd.merge(emp_df, emp_df, left_on='MGR', right_on='EMPNO')
    print(mgr_empno_inner)

    mgr_empno_left= pd.merge(emp_df, emp_df, how='left', left_on='MGR', right_on='EMPNO')
    print(mgr_empno_left)

    mgr_empno_right = pd.merge(emp_df, emp_df, how='right', left_on='MGR', right_on='EMPNO')
    print(mgr_empno_right)
    print(mgr_empno_right[['EMPNO_x', 'ENAME_x', "MGR_x", 'EMPNO_y', 'ENAME_y']])







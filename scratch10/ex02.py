import pandas as pd
import cx_Oracle
from scratch09.ex10 import select_all_from


def peak_to_peak(x):
    return x.max() - x.min()


if __name__ == '__main__':
    dsn = cx_Oracle.makedsn('localhost', 1521, 'orcl')
    with cx_Oracle.connect('scott', 'tiger', dsn) as connection:
        with connection.cursor() as cursor:
            emp_df = select_all_from('emp', cursor)
            print(emp_df)
            emp_df.to_csv('emp_df.csv', index=False)

    grouped_deptno = emp_df.groupby('DEPTNO')
    print('\n1) 부서별 평균 급여')
    print(grouped_deptno['SAL'].mean())

    print('\n2) 부서별 인원수')
    print(grouped_deptno['EMPNO'].count())

    print('\n3) 부서별 급여 최소값')
    print(grouped_deptno['SAL'].min())

    print('\n4) 부서별 급여 최대값')
    print(grouped_deptno['SAL'].max())

    print('\n5) 부서별 데이터프레임')
    df_groupde_deptno = pd.DataFrame({
        'count': grouped_deptno['EMPNO'].count(),
        'mean_sal': grouped_deptno['SAL'].mean(),
        'min_sal': grouped_deptno['SAL'].min(),
        'max_sal': grouped_deptno['SAL'].max()
    })
    print(df_groupde_deptno)

    df_groupde_deptno = grouped_deptno['SAL'].agg(['count', 'mean', 'min', 'max', peak_to_peak])
    print(df_groupde_deptno)

    grouped_mgr = emp_df.groupby('MGR')
    print(grouped_mgr)
    print('\n6) 매니저별 평균 급여')
    print(grouped_mgr['SAL'].mean())

    print('\n7) 매니저별 인원수')
    print(grouped_mgr['EMPNO'].count())

    print('\n8) 매니저별 급여 최소값')
    print(grouped_mgr['SAL'].min())

    print('\n9) 매니저별 급여 최대값')
    print(grouped_mgr['SAL'].max())

    print('\n10) 매니저별 데이터프레임')
    df_groupde_mgr = pd.DataFrame({
        'count': grouped_mgr['EMPNO'].count(),
        'mean_sal': grouped_mgr['SAL'].mean(),
        'min_sal': grouped_mgr['SAL'].min(),
        'max_sal': grouped_mgr['SAL'].max()
    })
    print(df_groupde_mgr)

    grouped_job = emp_df.groupby('JOB')
    print(grouped_job)
    print('\n11) 직책별 평균 급여')
    print(grouped_job['SAL'].mean())

    print('\n12) 직책별 인원수')
    print(grouped_job['EMPNO'].count())

    print('\n13) 직책별 급여 최소값')
    print(grouped_job['SAL'].min())

    print('\n14) 직책별 급여 최대값')
    print(grouped_job['SAL'].max())

    print('\n15) 직책별 데이터프레임')
    df_groupde_job = pd.DataFrame({
        'count': grouped_job['EMPNO'].count(),
        'mean_sal': grouped_job['SAL'].mean(),
        'min_sal': grouped_job['SAL'].min(),
        'max_sal': grouped_job['SAL'].max()
    })
    print(df_groupde_job)
    print(grouped_job['SAL'].agg(['count', 'mean', 'min', 'max', lambda x: x.max() - x.min()]))

    print('\n16) 부서별, 직책별 데이터프레임')
    groupde_deptno_job = emp_df.groupby(['DEPTNO', 'JOB'])
    df_groupde_deptno_job = pd.DataFrame({
        'count': groupde_deptno_job['EMPNO'].count(),
        'mean_sal': groupde_deptno_job['SAL'].mean(),
        'min_sal': groupde_deptno_job['SAL'].min(),
        'max_sal': groupde_deptno_job['SAL'].max()
    })
    print(df_groupde_deptno_job)
    print(groupde_deptno_job['SAL'].agg(['count', 'mean', 'min', 'max']))
    print(groupde_deptno_job['SAL'].agg(Count='count', Mean='mean', Min='min', Max='max',
                                        Range=lambda x: x.max() - x.min()))

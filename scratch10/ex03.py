import pandas as pd

if __name__ == '__main__':
    # csv파일에서 데이터 프레임 생성
    emp_df = pd.read_csv('emp_df', encoding='UTF-8')
    print(emp_df.iloc[0:5])
    print()

    # 부서별, 직책별 직원 수 출력
    grouped = emp_df.groupby(['DEPTNO', 'JOB'])
    emp_deptno_job = grouped['EMPNO']
    result_df = emp_deptno_job.agg('count')
    print(result_df)
    print()
    print(result_df.unstack())
    print(result_df.unstack().shape)

    grouped = emp_df.groupby(['DEPTNO', 'JOB'], as_index=False)
    print(grouped['EMPNO'].count())

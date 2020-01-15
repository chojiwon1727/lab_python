import pandas as pd

if __name__ == '__main__':
    names = ['EMPNO', 'ENAME', 'JOB', 'MGR', 'HIREDATE', 'SAL', 'COMM', 'DEPTNO']
    emp = pd.read_csv('emp.csv', encoding='UTF-8', names=names)
    print(emp)

    # 1) 급여(sal)가 2000이상인 직원들의 모든 정보 출력
    print('\n1) 급여(sal)가 2000이상인 직원들의 모든 정보 출력')
    sal_2000 = emp[emp['SAL'] >= 2000]
    print(sal_2000)

    # 2) 부서번호(deptno)가 10번인 직원들의 모든 정보 출력
    print('\n2) 부서번호(deptno)가 10번인 직원들의 모든 정보 출력')
    deptno_10 = emp[emp['DEPTNO'] == 10]
    print(deptno_10)

    # 3) 급여가 전체 직원 급여의 평균보다 많은 직원의 사번, 이름, 급여 출력
    print('\n3) 급여가 전체 직원 급여의 평균보다 많은 직원의 사번, 이름, 급여 출력')
    mean_sal = emp['SAL'].mean()
    print(f'\t* 전체 직원 급여의 평균 : {mean_sal}')
    emp_mean_sal = emp[emp['SAL'] > mean_sal]
    print(emp_mean_sal[['EMPNO', 'ENAME', 'SAL']])

    # 4) 30번 부서에서 일하는 직책이 ‘SALESMAN’인 직원들의 사번, 이름, 급여, 부서번호 출력
    print('\n4) 30번 부서에서 일하는 직책이 ‘SALESMAN’인 직원들의 사번, 이름, 급여, 부서번호 출력')
    deptno_30 = emp[emp['DEPTNO'] == 30]
    deptno_30_salesman = deptno_30[deptno_30['JOB'] == 'SALESMAN']
    print(deptno_30_salesman[['EMPNO', 'ENAME', 'SAL', 'DEPTNO']])

    # 5) 20,30번 부서에서 근무하는 직원들 중 급여가 2000을 초과하는 직원들의 사번, 이름, 급여, 부서번호 출력
    print('\n5) 20,30번 부서에서 근무하는 직원들 중 급여가 2000을 초과하는 직원들의 사번, 이름, 급여, 부서번호 출력')
    deptno_20 = emp[emp['DEPTNO'] == 20]
    deptno_30 = emp[emp['DEPTNO'] == 30]
    deptno_20_30 = pd.concat([deptno_20, deptno_30], ignore_index=True)
    sal2000_dept2030 = deptno_20_30[deptno_20_30['SAL'] > 2000]
    print(sal2000_dept2030[['EMPNO', 'ENAME', 'SAL', 'DEPTNO']])

    # 동일한 결과--> deptno_20_30 = emp[(emp['DEPTNO'] == 20) | (emp['DEPTNO'] == 30)]
    #  deptno_20_30 = emp[emp['DEPTNO'].isin[20,30]]

    # 6) 수당(comm)이 없는 직원들 중에서, 매니저(mgr)가 있고 직책이 ‘MANAGER’ 또는 ‘CLERK’인 직원들의 모든 정보 출력
    print('\n6) 수당(comm)이 없는 직원들 중에서, 매니저(mgr)가 있고 직책이 ‘MANAGER’ 또는 ‘CLERK’인 직원들의 모든 정보 출력')
    comm_isnull = emp[emp['COMM'].isnull()]            # -> numpy.isnan(emp['COMM'])
    comm_mgr = comm_isnull[comm_isnull['MGR'].notnull()]
    comm_mgr_manager = comm_mgr[comm_mgr['JOB'] == 'MANAGER']
    comm_mgr_clerk = comm_mgr[comm_mgr['JOB'] == 'CLERK']
    comm_mgr_job = pd.concat([comm_mgr_manager, comm_mgr_clerk], ignore_index=True)
    print(comm_mgr_job)

    # 동일한 결과--> comm_mgr_job = comm_mgr[(comm_mgr['JOB'] == 'MANAGER') | (comm_mgr['JOB'] == 'CLERK')]

    # 7) 사원 이름에 영문자 ‘E’가 포함된 직원들의 이름 출력(str.contains() 사용하기)
    print('\n7) 사원 이름에 영문자 ‘E’가 포함된 직원들의 이름 출력(str.contains() 사용하기)')
    ename_e = emp[emp['ENAME'].str.contains('E')]
    print(ename_e['ENAME'])

    # 8) DataFrame을 csv파일 형식으로 파일에 write하는 함수를 찾아서 실행하기
    print('\n8) DataFrame을 csv파일 형식으로 파일에 write하는 함수를 찾아서 실행하기')
    emp.to_csv('emp2.csv', index=False)
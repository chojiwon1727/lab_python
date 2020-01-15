import cx_Oracle
import lec08_darabase.oracle_comfig as cfg

with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as connection:
    with connection.cursor() as cursor:
        deptno = int(input('부서번호를 입력하세요>>'))
        sql1 = 'select empno, ename, deptno from emp where deptno = :0'
        cursor.execute(sql1, [deptno])
        for row in cursor:
            print(row)

        print('================')

        alpha = input('알파벳을 입력하세요>>')
        sql2 = 'select empno, ename, sal from emp where upper(ename) like :ename'
        alpha = alpha.upper()
        alpha = '%' + alpha + '%'
        cursor.execute(sql2, ename=alpha)
        for row1 in cursor:
            print(row1)

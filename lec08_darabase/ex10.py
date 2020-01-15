import cx_Oracle
import lec08_darabase.oracle_comfig as cfg

with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as connectione:
    with connectione.cursor() as cursor:
        deptno = int(input("부서번호를 입력하세요>>"))
        sql1 = """ select e.empno, e.ename, e.sal, e.deptno, d.dname
                   from emp e, dept d
                   where e.deptno = d.deptno
                   and e.deptno = :deptno"""

        sql_ansi = """ select e.empno, e.ename, e.sal, e.deptno, d.dname
                   from emp e join dept d
                   on e.deptno = d.deptno
                   where e.deptno = :deptno"""

        cursor.execute(sql1, deptno=deptno)
        for row in cursor:
            print(row)
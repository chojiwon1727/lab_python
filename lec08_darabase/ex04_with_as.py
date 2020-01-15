import cx_Oracle
import lec08_darabase.oracle_comfig as cfg

with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as conn:
    with conn.cursor() as cursor:
        cursor.execute('select empno, ename, deptno from emp')
        for row in cursor:
            print(row)


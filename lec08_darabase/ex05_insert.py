import cx_Oracle
import lec08_darabase.oracle_comfig as cfg

with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as connection:
    with connection.cursor() as cursor:
        sql_insert = "insert into dept2(deptno, dname, loc) values(91, '강의장10번', 'Seoul')"
        cursor.execute(sql_insert)

        sql_select = 'select * from dept2'
        cursor.execute(sql_select)
        for row in cursor:
            print(row)
        connection.commit()
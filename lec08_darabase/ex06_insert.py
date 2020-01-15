import cx_Oracle
import lec08_darabase.oracle_comfig as cfg

with cx_Oracle.connect(cfg.user, cfg.pwd,cfg.dsn) as connection:
    with connection.cursor() as cursor:
        deptno = int(input('부서 번호 입력>>'))
        dname = input('부서 이름 입력>>')
        loc = input('부서 위치 입력>>')

        sql_insert = f"insert into dept2 values({deptno}, '{dname}', '{loc}')"
        cursor.execute(sql_insert)
        connection.commit()

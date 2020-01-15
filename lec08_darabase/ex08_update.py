"""
dept2테이블에서 deptno를 입력받아서 해당 부서의 loc를 update 실행
"""
import cx_Oracle
import lec08_darabase.oracle_comfig as cfg

with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as connection:
    with connection.cursor() as cursor:
        deptno = int(input('부서 번호를 입력하세요>>'))
        loc = input('변경할 부서 위치를 입력하세요>>')

        sql1 = 'update dept2 ' \
               'set loc = :0 ' \
               'where deptno = :1'

        cursor.execute(sql1, [loc, deptno])

        connection.commit()




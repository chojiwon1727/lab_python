import cx_Oracle
import lec08_darabase.oracle_comfig as cfg

connection = cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn)
cursor = connection.cursor()

cursor.execute('select*from dept')
for row in cursor:
    print(row)


cursor.close()
connection.close()
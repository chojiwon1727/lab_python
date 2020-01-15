import cx_Oracle
import lec08_darabase.oracle_comfig as cfg

connection = cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn)

cursor = connection.cursor()

cursor.execute('select * from emp')
row = cursor.fetchone()
while row:
    print(row)
    row = cursor.fetchone()
# while True:
#     row = cursor.fetchone()
#     if row is None:
#         break
#     print(row)


cursor.close()

# print('DB version:', connection.version)

connection.close()
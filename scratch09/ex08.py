import cx_Oracle
import lec08_darabase.oracle_comfig as cfg
import csv

# DSN : Data Source Name
# dsn = cx_Oracle.makedsn('localhost', 1521, 'orcl')

if __name__ == '__main__':
    connection = cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn)
    cursor = connection.cursor()

    cursor.execute('select * from emp')
    emp = [row for row in cursor]
    with open('emp.csv', mode='w', encoding='UTF-8', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        for row in emp:
            writer.writerow(row)

    cursor.close()
    connection.close()



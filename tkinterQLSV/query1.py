from mysql.connector import MySQLConnection, Error
from configDb import read_db_config

# fetchone()
# fetchmany()
# fetchall()


def query_with_fetchone():
    data = []
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")

        row = cursor.fetchone()

        while row is not None:
            # print(row)
            data.append(row)
            row = cursor.fetchone()

        print(data)
        return data

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def query_with_fetchall():
    data = []
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        rows = cursor.fetchall()

        print('Total Row(s):', cursor.rowcount)
        for row in rows:
            data.append(row)
            print(row)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def iter_row(cursor, size=10):
    while True:
        rows = cursor.fetchmany(size)
        print(rows)
        if not rows:
            break
        for row in rows:

            yield row


def query_with_fetchmany():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM books")

        for row in iter_row(cursor, 10):
            # print(row)
            pass

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    # query_with_fetchone()
    # query_with_fetchall()
    query_with_fetchmany()

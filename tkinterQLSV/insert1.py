from mysql.connector import MySQLConnection, Error
from configDb import read_db_config
import json


def insert_book(id, name, author):
    query = "INSERT INTO `books`(`id`, `name`, `author`) " \
            "VALUES(%s,%s,%s)"
    args = (id, name, author)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)
        # print('Check status: ', cursor.lastrowid)
        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()


def insert_books(books):
    query = "INSERT INTO `books`(`id`, `name`, `author`) " \
            "VALUES(%s,%s,%s)"

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.executemany(query, books)

        conn.commit()
    except Error as e:
        print('Error:', e)

    finally:
        cursor.close()
        conn.close()

# data = '{"id": "13", "name": "name","author": "author"}'
# jdata = json.loads(data)
# # print(jdata)


books = [('15', 'name', 'author'), ('16', 'name',
                                    'author'), ('17', 'name', 'author')]


def main():
    # insert_book('14', 'name', 'author')
    insert_books(books)


if __name__ == '__main__':
    main()

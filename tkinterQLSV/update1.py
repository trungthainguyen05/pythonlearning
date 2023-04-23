from mysql.connector import MySQLConnection, Error
from configDb import read_db_config


def update_book(name, author, id):
    # read database configuration
    db_config = read_db_config()

    # prepare query and data
    query = """ UPDATE `books`
                SET `name`= %s,`author`= %s
                WHERE `id` = %s """

    data = (name, author, id)

    try:
        conn = MySQLConnection(**db_config)

        # update book title
        cursor = conn.cursor()
        cursor.execute(query, data)

        # accept the changes
        conn.commit()

    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    update_book('name2', 'author2', '17')

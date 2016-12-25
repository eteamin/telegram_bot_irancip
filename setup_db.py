import sqlite3

from src.variables import path_to_db


if __name__ == '__main__':
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()

    try:
        # Create the db
        cursor.execute(
            """
            CREATE TABLE tokens (id int primary_key, telegram_uid char, code_hash char, expired bool);
            """
        )
    except sqlite3.OperationalError as ex:
        print('Creating db failed due to %s' % str(ex))

    connection.commit()

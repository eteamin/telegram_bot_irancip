import sqlite3

from src.model.user import User
from src.variables import path_to_db

connection = sqlite3.connect(path_to_db)
cursor = connection.cursor()


def insert_telegram_user(tg_id):
    user = User(telegram_user_id=tg_id)
    values = (user.tg_id, user.hashed_discount_code, False)
    cursor.execute(
        '''
        INSERT INTO tokens (telegram_uid, code_hash, expired) VALUES (?, ?, ?);
        ''',
        values
    )
    try:
        connection.commit()
    except sqlite3.IntegrityError:
        pass


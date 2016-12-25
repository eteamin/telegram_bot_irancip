import sqlite3

from src.variables import path_to_db
from src.model.user import User


connection = sqlite3.connect(path_to_db)
cursor = connection.cursor()


def select_telegram_id(telegram_uid, token):
    query_result = cursor.execute(
        """
        SELECT * FROM tokens WHERE telegram_uid = (?)
        """,
        (telegram_uid, )
    ).fetchone()
    if query_result:
        user = User(query_result[1])
        return True if user.validate_discount_code(token) else False
    else:
        return False

import os
from hashlib import sha256


class User(object):
    def __init__(self, telegram_user_id):
        self.tg_id = telegram_user_id
        self.discount_code = self.generate_discount_code()
        self.hashed_discount_code = self.hash_discount_code()

    def generate_discount_code(self):
        salt = sha256()
        salt.update(os.urandom(60))
        salt = salt.hexdigest()
        return salt[:12]

    def hash_discount_code(self):
        salt = sha256()
        salt.update(os.urandom(60))
        salt = salt.hexdigest()
        hash = sha256()
        hash.update((self.discount_code + salt).encode('utf-8'))
        hash = hash.hexdigest()
        result = salt + hash
        return result

    def validate_discount_code(self, provided_code):
        hash = sha256()
        hash.update((provided_code + self.discount_code[:64]).encode('utf-8'))
        return self.discount_code[:64] == hash.hexdigest()

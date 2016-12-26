import requests
from pyDes import triple_des

from src.variables import auth_message, auth_secret_key, api_url


def headers():
    return {'token': triple_des(auth_secret_key).encrypt(auth_message, padmode=2)}


def post_uid(telegram_uid):
    """
    Posting telegram_uid to API to get a token
    {
        telegram_uid
    }
    :param telegram_uid: :type: Str
    :return: discount_token :type: Str
    """
    payload = {
        'telegram_uid': telegram_uid
    }
    return requests.post('%s/users/%s' % (api_url, telegram_uid), payload).json()['discount_token']

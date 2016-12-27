from json.decoder import JSONDecodeError

import requests
from pyDes import triple_des

from src.variables import auth_message, auth_secret_key, api_url


def headers():
    return {'token': triple_des(auth_secret_key).encrypt(auth_message, padmode=2)}


def post_uid(telegram_uid, telegram_name):
    """
    Posting telegram_uid to API to get a token
    {
        telegram_uid
    }
    :param telegram_uid: :type: Str
    :param telegram_name: :type: Str

    :return: status :type: dict
    """
    payload = {
        'telegram_uid': telegram_uid,
        'telegram_name': telegram_name
    }
    try:
        resp = requests.post('%s/users/' % api_url, json=payload).json()
    except JSONDecodeError:
        return {
            'OK': False,
            'Error': 'لطفا مجددا تلاش کنید'
        }
    if 'token' in resp:
        return {
            'OK': True,
            'Error': None,
            'token': resp['token']
        }
    else:
        return {
            'OK': False,
            'Error': resp['detail']
        }


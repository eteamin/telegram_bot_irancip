# -*- coding: utf-8 -*-

import sys
from setuptools import setup, find_packages
py_version = sys.version_info[:2]


install_requires = [
    'pyDes',
    'python-telegram-bot',
    'requests'
]

setup(
    name='irancip_bot',
    version='0.1-dev',
    description='',
    author='eteamin',
    author_email='aminetesamian1371@gmail.com',
    url='https://github.com/eteamin/telegram_bot_irancip',
    packages=find_packages(),
    install_requires=install_requires,
)
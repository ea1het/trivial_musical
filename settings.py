# -*- coding: utf-8 -*-
# pylint: disable=locally-disabled, multiple-statements
# pylint: disable=fixme, line-too-long, invalid-name
# pylint: disable=W0703

""" Trivial Musical """

__author__ = 'EA1HET, EA1GIY'
__date__ = '26/09/2020'


from os import path
from environs import Env


ENV_FILE = path.join(path.abspath(path.dirname(__file__)), '.env')

try:
    ENVIR = Env()
    ENVIR.read_env()
except Exception as e:
    print('Warning: .env file not found: %s' % e)


class Config:
    """ This is the generic loader that sets common attributes and variables """
    JSON_SORT_KEYS = False

    ENV = ENVIR('ENV', 'Development')
    DEBUG = ENVIR.bool('DEBUG', False)
    TESTING = ENVIR.bool('TESTING', False)

    DB_HOST = ENVIR('DB_HOST', None)
    DB_PORT = ENVIR('DB_PORT', 3306)
    DB_USER = ENVIR('DB_USER', None)
    DB_PASSWORD = ENVIR('DB_PASSWORD', None)
    DB_DATABASE = ENVIR('DB_DATABASE', None)

    SECRET_KEY = ENVIR('SECRET_KEY') or 'NoSecretKeyDefined'

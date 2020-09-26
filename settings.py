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

    ENV = ENVIR('ENV')
    DEBUG = ENVIR('DEBUG')
    TESTING = ENVIR('TESTING')

    DB_HOST = ENVIR('DB_HOST')
    DB_USER = ENVIR('DB_USER')
    DB_PASSWORD = ENVIR('DB_PASSWORD')
    DB_DATABASE = ENVIR('DB_DATABASE')

    SECRET_KEY = ENVIR('SECRET_KEY') or 'NoSecretKeyDefined'

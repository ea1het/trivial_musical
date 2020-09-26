# -*- coding: utf-8 -*-
# pylint: disable=locally-disabled, multiple-statements
# pylint: disable=fixme, line-too-long, invalid-name
# pylint: disable=W0703

""" Trivial Musical """

__author__ = 'EA1HET, EA1GIY'
__date__ = '26/09/2020'


from os import environ, path
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
    DEBUG = True
    TESTING = True


class Development(Config):
    """ Development loader, instance of class Config """
    ENV = 'development'
    TESTING = False
    SECRET_KEY = ENVIR('DEV_SK') or 'NotDefined'
    DB_DICT = ENVIR('DEV_DB') or None


class Testing(Config):
    """ Testing loader, instance of class Config """
    ENV = 'testing'
    DEBUG = False
    SECRET_KEY = ENVIR('TST_SK') or 'NotDefined'
    DB_DICT = ENVIR('TST_DB') or None


class Production(Config):
    """ Production loader, instance of class Config """
    ENV = 'production'
    DEBUG = False
    TESTING = False
    try:
        SECRET_KEY = ENVIR('PRD_SK')
        DB_DICT = ENVIR('PRD_DB')
    except Exception as e:
        print(f'{e}\n\nProduction variables not defined. Cannot continue!')
        from sys import exit
        exit(1)

# -*- coding: utf-8 -*-
# pylint: disable=locally-disabled, multiple-statements
# pylint: disable=fixme, line-too-long, invalid-name
# pylint: disable=W0703

""" Project description """

__author__ = 'EA1HET'
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
    """
    This is the generic loader that sets common attributes

    :param: None
    :return: None
    """
    JSON_SORT_KEYS = False
    DEBUG = True
    TESTING = True


class Development(Config):
    """ Development loader """
    ENV = 'development'
    if environ.get('KEY_DEVL'):
        SECRET_KEY = ENVIR('KEY_DEVL')
    if environ.get('DATABASE_URI_DEVL'):
        DATABASE_URI = ENVIR('DATABASE_URI_DEVL')
    TESTING = False


class Testing(Config):
    """ Testing loader """
    ENV = 'testing'
    if environ.get('KEY_TEST'):
        SECRET_KEY = ENVIR('KEY_TEST')
    if environ.get('DATABASE_URI_TEST'):
        DATABASE_URI = ENVIR('DATABASE_URI_TEST')
    DEBUG = False


class Production(Config):
    """ Production loader """
    ENV = 'production'
    if environ.get('KEY_PROD'):
        SECRET_KEY = ENVIR('KEY_PROD')
    if environ.get('DATABASE_URI_PROD'):
        DATABASE_URI = ENVIR('DATABASE_URI_PROD')
    DEBUG = False
    TESTING = False

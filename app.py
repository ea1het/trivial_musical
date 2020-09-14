# -*- coding: utf-8 -*-
# pylint: disable=locally-disabled, multiple-statements
# pylint: disable=fixme, line-too-long, invalid-name
# pylint: disable=W0703

""" Trivial Musical """

__author__ = 'EA1HET, EA1GIY'
__date__ = '12/09/2020'

from fastapi import FastAPI
import uvicorn


title = 'Trivial Musical'
description = 'This is the backend for a simple trivial game'
version = '1.0'

APP = FastAPI(title=title, description=description, version=version, root_path='', redoc_url='')


@APP.get("/", name='Endpoint "Root"')
def index():

    data = {
        'tstamp': '',
        'url_base': '',
        'url_preguntas': ''
    }

    return data


@APP.get('/preguntas', name='Endpoint "Preguntas"')
def preguntas():
    """
    Endpoint for questions (preguntas)

    :param arg1: description
    :type arg1: type description
    :return: a dictionary
    """

    data = {'key': 'value'}

    return data


def main():
    uvicorn.run(APP, host='127.0.0.1', port=5000)


if __name__ == '__main__':
    main()

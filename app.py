# -*- coding: utf-8 -*-
# pylint: disable=locally-disabled, multiple-statements
# pylint: disable=fixme, line-too-long, invalid-name
# pylint: disable=W0703

""" Trivial Musical """

__author__ = 'EA1HET'
__date__ = '12/09/2020'

from fastapi import FastAPI, Header, Request, Depends
import uvicorn


APP = FastAPI()


@APP.get('/preguntas')
def preguntas():
    """
    Endpoint for questions (preguntas)
    :param none
    :return dictionary: str
    """

    data = {'key': 'value'}
    return data


def main():
    uvicorn.run(APP, host='127.0.0.1', port=5000)


if __name__ == '__main__':
    main()

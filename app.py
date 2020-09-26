# -*- coding: utf-8 -*-
# pylint: disable=locally-disabled, multiple-statements
# pylint: disable=fixme, line-too-long, invalid-name
# pylint: disable=W0703

""" Trivial Musical """

__author__ = 'EA1HET, EA1GIY'
__date__ = '12/09/2020'

from os import environ
from flask import Flask, make_response, url_for
from datetime import datetime
import settings


# -- Application initialization. ---------------------------------------------
__modeConfig__ = environ.get('MODE_CONFIG') or 'Development'

APP = Flask('trivial_musical')
APP.config.from_object(getattr(settings, __modeConfig__.title()))

# -- This functions control how to respond to common errors. -----------------
@APP.errorhandler(404)
def not_found(error):
    """ HTTP Error 404 Not Found """
    data = {
        'error': 'true',
        'msg': str(error),
        'base_url': url_for('index', _external=True)
    }
    headers = {}
    return make_response(data, 404, headers)


@APP.errorhandler(405)
def not_allowed(error):
    """ HTTP Error 405 Not Allowed """
    data = {
        'error': 'true',
        'msg': str(error)
    }
    headers = {}
    return make_response(data, 405, headers)


@APP.errorhandler(500)
def internal_error(error):
    """ HTTP Error 500 Internal Server Error """
    data = {
        'error': 'true',
        'msg': str(error)
    }
    headers = {}
    return make_response(data, 500, headers)


# -- This piece of code controls what happens during the HTTP transaction. ---
@APP.before_request
def before_request():
    """ This function handles HTTP request as it arrives to the API """
    pass


@APP.after_request
def after_request(response):
    """ This function handles HTTP response before send it back to client  """
    return response


# -- This is where the API effectively starts. -------------------------------
@APP.route('/preguntas', methods=['GET'])
def get_preguntas():
    """ TBD """
    data = {
        'tstamp': datetime.utcnow().timestamp(),
        'base_url': url_for('index', _external=True)
    }
    headers = {}
    return make_response(data, 200, headers)


@APP.route('/preguntas', methods=['POST'])
def post_preguntas():
    """ TBD """
    pass


@APP.route('/niveles', methods=['POST'])
def post_niveles():
    """ TBD """
    pass


@APP.route('/tiempos', methods=['POST'])
def post_tiempos():
    """ TBD """
    pass


@APP.route('/categorias/subcategorias', methods=['POST'])
def post_subcategorias():
    """ TBD """
    pass


@APP.route('/categorias', methods=['POST'])
def post_categorias():
    """ TBD """
    pass


@APP.route('/', methods=['GET'])
def index():
    """ This is the main function of the / endpoint """

    # Put now your code here

    data = {
        'tstamp': datetime.utcnow().timestamp(),
        'url_base': url_for('index', _external=True),
        'url_preguntas': url_for('get_preguntas', _external=True)
    }
    headers = {
        'MyHeader': 'MyHeaderValueHere'
    }
    return make_response(data, 200, headers)


def main():
    APP.run(host='0.0.0.0', port=5000)


# -- This is The main programme instantiation -_------------------------------
if __name__ == '__main__':
    main()

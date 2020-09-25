# -*- coding: utf-8 -*-
# pylint: disable=locally-disabled, multiple-statements
# pylint: disable=fixme, line-too-long, invalid-name
# pylint: disable=W0703

""" Trivial Musical """

__author__ = 'EA1HET, EA1GIY'
__date__ = '12/09/2020'

from flask import Flask, jsonify, make_response


# -- Application initialization. ---------------------------------------------

APP = Flask('trivial_musical')


# -- This function controls how to respond to common errors. -----------------

@APP.errorhandler(404)
def not_found(error):
    """ HTTP Error 404 Not Found """
    headers = {}
    return make_response(
        jsonify(
            {
                'error': 'true',
                'msg': str(error)
            }
        ), 404, headers
    )


@APP.errorhandler(405)
def not_allowed(error):
    """ HTTP Error 405 Not Allowed """
    headers = {}
    return make_response(
        jsonify(
            {
                'error': 'true',
                'msg': str(error)
            }
        ), 405, headers
    )


@APP.errorhandler(500)
def internal_error(error):
    """ HTTP Error 500 Internal Server Error """
    headers = {}
    return make_response(
        jsonify(
            {
                'error': 'true',
                'msg': str(error)
            }
        ), 500, headers
    )


# -- This piece of code controls what happens during the HTTP transaction. ---

@APP.before_request
def before_request():
    """ This function handles  HTTP request as it arrives to the API """
    pass


@APP.after_request
def after_request(response):
    """ This function handles HTTP response before send it back to client  """
    return response


# -- This is where the API effectively starts. -------------------------------

@APP.route('/', methods=['GET'])
def index():
    """ This is the main function of the / endpoint """

    # Put now your code here

    data = {
        'tstamp': '',
        'url_base': '',
        'url_preguntas': ''
    }

    headers = {
        'MyHeader': 'MyHeaderValueHere'
    }

    return make_response(
        jsonify(
            data
        ), 200, headers)


def main():
    APP.run(host='0.0.0.0', port=5000, debug=True, load_dotenv=True)


if __name__ == '__main__':
    main()

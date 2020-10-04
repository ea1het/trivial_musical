# -*- coding: utf-8 -*-
# pylint: disable=locally-disabled, multiple-statements
# pylint: disable=fixme, line-too-long, invalid-name
# pylint: disable=wrong-spelling-in-comment
# pylint: disable=W0703

""" Trivial Musical """

__author__ = 'EA1HET, EA1GIY'
__date__ = '12/09/2020'


from flask import Flask, make_response, url_for, request
from datetime import datetime
from cerberus import Validator
import psycopg2
import settings


# -- Application initialization. ---------------------------------------------s
APP = Flask('trivial_musical')
APP.config.from_object(getattr(settings, 'Config'))


# -- Incoming data validation with Cerberus. ---------------------------------
schema_categoria = {
    'categoria': {'type': 'string', 'empty': False}
}


# -- Database connection initialization. -------------------------------------
def db_connect():
    db = f'host={settings.Config.DB_HOST} ' \
         f'port={settings.Config.DB_PORT} ' \
         f'user={settings.Config.DB_USER} ' \
         f'password={settings.Config.DB_PASSWORD} ' \
         f'dbname={settings.Config.DB_DATABASE}'
    c = psycopg2.connect(db)
    return c


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
@APP.route('/preguntas', methods=['GET', 'POST'])
def preguntas():
    """ TBD """

    # If request methos was POST...
    if request.method == 'POST':
        data = {'Method': 'POST'}
        headers = {}
        return make_response(data, 200, headers)

    # ... otherwise, defaults to GET method
    data = {
        'tstamp': datetime.utcnow().timestamp(),
        'base_url': url_for('index', _external=True)
    }
    headers = {}

    return make_response(data, 200, headers)


@APP.route('/niveles', methods=['GET', 'POST'])
def niveles():
    """ Return the full list of 'niveles' defined (should be a little """

    # If request methos was POST...
    if request.method == 'POST':
        data = {'Method': 'POST'}
        headers = {}
        return make_response(data, 200, headers)

    # ... otherwise, defaults to GET method
    data = {
        'tstamp': datetime.utcnow().timestamp(),
        'url_base': url_for('index', _external=True),
        'url_niveles': url_for('niveles', _external=True)
    }
    headers = {}
    return make_response(data, 200, headers)


@APP.route('/tiempos', methods=['GET', 'POST'])
def tiempos():
    """ TBD """
    pass


@APP.route('/categorias/subcategorias', methods=['GET', 'POST'])
def subcategorias():
    """ TBD """
    pass


@APP.route('/categorias', methods=['GET', 'POST', 'DELETE'])
def categorias():
    """ Categorias de las preguntas de Trivial """

    try:
        conn = db_connect()

        # If request method was POST ...
        if request.method == 'POST':
            with conn.cursor() as c:
                v = Validator(schema_categoria)
                doc = request.get_json()

                if v.validate(doc):
                    post_cat = request.get_json()['categoria']
                    sql = f"INSERT INTO trivial_schema.categorias (categoria, notas) " \
                          f"VALUES('{post_cat}', '');"
                    c.execute(sql)
                    conn.commit()
                    data = {
                        'result': 'ok',
                        'message': 'row successfully inserted into database'
                    }
                    http_code = 200
                else:
                    data = {
                        'result': 'ko',
                        'message': 'data mismatch',
                        'error': v.errors
                    }
                    http_code = 404
            headers = {}
            return make_response(data, http_code, headers)

        # ... eventually it can also be a DELETE ...
        elif request.method == 'DELETE':

            with conn.cursor() as c:
                v = Validator(schema_categoria)
                doc = request.get_json()

                if v.validate(doc):
                    del_cat = request.get_json()['categoria']
                    sql = f"DELETE FROM trivial_schema.categorias WHERE categoria = '{del_cat}';"
                    c.execute(sql)
                    conn.commit()
                    data = {
                        'result': 'ok',
                        'message': 'row successfully removed from database'
                    }
                    http_code = 200
                else:
                    data = {
                        'result': 'ko',
                        'message': 'data mismatch',
                        'error': v.errors
                    }
                    http_code = 405
            headers = {}
            return make_response(data, http_code, headers)

        # ... otherwise, defaults to GET method
        else:
            with conn.cursor() as c:
                sql = "SELECT * FROM trivial_schema.categorias;"
                c.execute(sql)
                res = c.fetchall()

            reg_dict = {}
            for _ in res:
                reg_dict[_[0]] = _[1]

            data = {
                'tstamp': datetime.utcnow().timestamp(),
                'url_base': url_for('index', _external=True),
                'url_niveles': url_for('categorias', _external=True),
                'registros': reg_dict
            }
            http_code = 200
            headers = {}
            return make_response(data, http_code, headers)

    except (Exception, psycopg2.DatabaseError) as e:
        print(e)
        data = {
            'result': 'ko',
            'message': 'server side error',
            'error': f'Error {e}'
        }
        headers = {}
        http_code = 500
        return make_response(data, http_code, headers)

    finally:
        print('pase por aqui')


@APP.route('/', methods=['GET'])
def index():
    """ This is the main function of the / endpoint """

    # Put now your code here

    data = {
        'tstamp': datetime.utcnow().timestamp(),
        'url_base': url_for('index', _external=True),
        'url_preguntas': url_for('preguntas', _external=True)
    }

    headers = {}
    return make_response(data, 200, headers)


def main():
    APP.run(host='0.0.0.0', port=5000)


# -- This is The main programme instantiation -_------------------------------
if __name__ == '__main__':
    main()

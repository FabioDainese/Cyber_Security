#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pymysql
from logging import FileHandler, Formatter, WARNING
from flask import Flask, render_template, abort, jsonify, g

from conf import host, logfile, debug, db_conf

app = Flask(__name__)
file_handler = FileHandler(logfile)
file_handler.setFormatter(Formatter(
    '%(asctime)s %(levelname)s: %(message)s '
    '[in %(pathname)s:%(lineno)d]'
))
file_handler.setLevel(WARNING)
app.logger.addHandler(file_handler)

def query_handler(sql, params, cur):
    try:
        cur.execute(sql, params)
    except pymysql.Error as e:
        code, message = e.args
        cur.close()
        app.logger.critical(e)
        abort(400, code)
    except Exception as e:
        cur.close()
        app.logger.critical(e)
        abort(500)

    return cur

def get_db_conn():
    db_conn = getattr(g, 'db_conn', None)
    db_conf['cursorclass'] = pymysql.cursors.DictCursor
    if db_conn is None:
        try:
            g.db_conn = pymysql.connect(**db_conf)
            db_conn = g.db_conn
        except pymysql.Error as e:
            app.logger.critical(e)
            sys.exit(1)
    return db_conn

@app.teardown_appcontext
def db_disconnect(exception=None, logger=app.logger):
    try:
        db_conn = getattr(g, 'db_conn', None)
        if db_conn is not None:
            db_conn.close()
    except Exception as e:
        app.logger.critical('Unable to close the database connection: {}'.format(e))
        sys.exit(1)

@app.errorhandler(403)
def access_denied(e):
    return render_template('error.html', msg=e), 403

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', msg=e), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('error.html', msg=e), 500

@app.errorhandler(400)
def myerr(error):
    return render_template('error.html', msg=error.description), 400

@app.route('/_get_releases/<col>/<int:page>')
def _get_releases(col, page):
    db_conn = get_db_conn()
    cur = db_conn.cursor()
    cur = query_handler('''
        SELECT * FROM releases
        ORDER BY {} ASC 
        LIMIT 10 OFFSET %s
        '''.format(col), [page*10], cur)
    releases = cur.fetchall()
    cur.close()
    if releases is None or len(releases) == 0:
        abort(404)

    return jsonify({'records': releases})

@app.route('/_get_djset/<int:set_id>')
def _get_djset(set_id):
    db_conn = get_db_conn()
    cur = db_conn.cursor()
    cur = query_handler('SELECT * FROM sets WHERE id = %s',
                        [set_id], cur)
    djset = cur.fetchone()
    cur.close()
    if djset is None:
        abort(404)
    
    return jsonify(djset)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host=host, debug=debug)
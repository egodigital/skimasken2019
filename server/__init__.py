from flask import Flask, jsonify, make_response, send_from_directory
import os
from os.path import exists, join, dirname, abspath
from http import HTTPStatus
import sys
import logging
import logging.config

from server.extensions.database import db
from server.extensions.migrate import migrate
from server.extensions.marshmallow import ma
from server.extensions.login import login_manager
from server.api import api
from server.models import *


def setup_logging(CONFIG_FILE, stdout=False):
    global log
    log_file_path = join(dirname(abspath(__file__)), CONFIG_FILE)
    logging.config.fileConfig(log_file_path, disable_existing_loggers=False)
    log = logging.getLogger(__name__)
    if stdout:
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        log.addHandler(handler)

def create_app(config):
    setup_logging(config.LOGGING_CONFIG, config.TESTING is True)
    log.info("-" * 25 + " Creating flask app " + "-" * 25)
    log.info(f"logging config: {config.LOGGING_CONFIG} loaded")

    app = Flask(__name__, static_folder='build')
    log.info(f"loading flask config: {config.__name__}")
    app.config.from_object(config)

    # Extensions initialisieren
    log.info("Initialize extensions...")
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db, render_as_batch=True, compare_type=True)
    api.init_app(app)
    login_manager.init_app(app)


    # Catching all routes
    # This route is used to serve all the routes in the frontend application after deployment.
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def catch_all(path):
        file_to_serve = path if path and exists(join(app.static_folder, path)) else 'index.html'
        return send_from_directory(app.static_folder, file_to_serve)

    # Error Handler
    @app.errorhandler(404)
    def page_not_found(error):
        json_response = jsonify({'error': 'Page not found'})
        return make_response(json_response, HTTPStatus.NOT_FOUND)

    log.info("Flask app created.")
    return app
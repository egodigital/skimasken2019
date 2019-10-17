import requests
import random
import logging
from http import HTTPStatus
from flask_restplus import Namespace
from flask_restplus import Resource

log = logging.getLogger(__name__)
api = Namespace('user', description='User related enpoints.')

@api.route('/')
class User(Resource):
    def get(self):
        log.info("test")
        return "Test", HTTPStatus.OK

import requests
import random
import logging
from http import HTTPStatus
from flask import request
from flask_restplus import Namespace
from flask_restplus import Resource

from server.models.user import UserModel, user_schema, users_schema, user_parser
from server.extensions.database import db

log = logging.getLogger(__name__)
api = Namespace('user', description='User related enpoints.')

@api.route('/<string:email>')
class User(Resource):
    def get(self, email):
        user = UserModel.query.filter(UserModel.email == email).first()
        return user_schema.dump(user), HTTPStatus.OK

    def delete(self, email):
        user = UserModel.query.filter(UserModel.email == email).first()
        if user:
            db.session.delete(user)
            db.session.commit()
        return "", HTTPStatus.NO_CONTENT

@api.route('/')
class UserList(Resource):
    def get(self):
        return users_schema.dump(UserModel.query.all()), HTTPStatus.OK

    @api.expect(user_parser)
    def post(self):
        user = user_schema.load(user_parser.parse_args(), session=db.session)
        db.session.add(user)
        db.session.commit()
        return user_schema.dump(user), HTTPStatus.CREATED

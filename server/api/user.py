import requests
import logging
from http import HTTPStatus
from flask import request, current_app
from flask_restplus import Namespace
from flask_restplus import Resource
from flask_restplus import reqparse
import flask_login

from server.models.user import UserModel, user_schema, users_schema, user_parser
from server.extensions.database import db
from server.extensions.login import login_manager

log = logging.getLogger(__name__)
api = Namespace('user', description='User related enpoints.')

@login_manager.user_loader
def load_user(user_id):
    return UserModel.query.filter(UserModel.email == user_id).first()

@api.route('/<string:email>')
class User(Resource):
    @flask_login.login_required
    @api.doc(responses={
        HTTPStatus.OK: 'Success',
        HTTPStatus.UNAUTHORIZED: 'Not authorized'
    })
    def get(self, email):
        user = UserModel.query.filter(UserModel.email == email).first()
        return user_schema.dump(user), HTTPStatus.OK

    @flask_login.login_required
    @api.doc(responses={
        HTTPStatus.OK: 'Success',
        HTTPStatus.UNAUTHORIZED: 'Not authorized'
    })
    def delete(self, email):
        user = UserModel.query.filter(UserModel.email == email).first()
        if user:
            db.session.delete(user)
            db.session.commit()
        return "", HTTPStatus.NO_CONTENT

@api.route('/')
class UserList(Resource):
    @flask_login.login_required
    @api.doc(responses={
        HTTPStatus.OK: 'Success',
        HTTPStatus.UNAUTHORIZED: 'Not authorized'
    })
    def get(self):
        env = flask_login.current_user.environment_id
        return users_schema.dump(UserModel.query.filter(UserModel.environment_id == env).all()), HTTPStatus.OK

    @api.expect(user_parser)
    def post(self):
        args = user_parser.parse_args()
        response = requests.get(current_app.config["API_BASE"] + "/environments", headers={"X-Api-Key": current_app.config["API_KEY"]})
        args["environment_id"] = response.json()["data"][0]["id"] # Hardcoded
        user = user_schema.load(args, session=db.session)
        db.session.add(user)
        db.session.commit()
        return user_schema.dump(user), HTTPStatus.CREATED

login_parser = reqparse.RequestParser()
login_parser.add_argument('email', type=str, required=True, location="json")
login_parser.add_argument('password', type=str, required=True, location="json")

@api.route('/me')
class UserLogin(Resource):
    @flask_login.login_required
    @api.doc(responses={
        HTTPStatus.OK: 'Success',
        HTTPStatus.UNAUTHORIZED: 'Not authorized'
    })
    def get(self):
        return user_schema.dump(flask_login.current_user), HTTPStatus.OK

    @api.expect(login_parser)
    @api.doc(responses={
        HTTPStatus.OK: 'Success',
        HTTPStatus.UNAUTHORIZED: 'Authentication failed'
    })
    def post(self):
        args = login_parser.parse_args()
        user = UserModel.query.filter(UserModel.email == args["email"]).first()
        if user is None and user.check_password(args["password"]):
            return "", HTTPStatus.UNAUTHORIZED
        flask_login.login_user(user)
        return user_schema.dump(user), HTTPStatus.OK

    @flask_login.login_required
    @api.doc(responses={
        HTTPStatus.OK: 'Success',
        HTTPStatus.UNAUTHORIZED: 'Not authorized'
    })
    def delete(self):
        flask_login.logout_user()
        return "", HTTPStatus.NO_CONTENT

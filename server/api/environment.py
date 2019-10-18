import requests
import logging
from http import HTTPStatus
from flask import request, current_app
from flask_restplus import Namespace
from flask_restplus import Resource
import flask_login


log = logging.getLogger(__name__)
api = Namespace('environment', description='Get the environment for the logged in user.')

@api.route('/')
class Environment(Resource):
    @flask_login.login_required
    @api.doc(responses={
        HTTPStatus.OK: 'Success',
        HTTPStatus.UNAUTHORIZED: 'Not authorized'
    })
    def get(self):
        user = flask_login.current_user
        response = requests.get(current_app.config["API_BASE"] + f"/environments", headers={"X-Api-Key": current_app.config["API_KEY"]})
        return [env for env in response.json()["data"] if env["id"] == user.environment_id][0], response.status_code

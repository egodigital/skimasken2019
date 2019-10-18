import requests
import logging
from http import HTTPStatus
from flask import request, current_app
from flask_restplus import Namespace
from flask_restplus import Resource
import flask_login


log = logging.getLogger(__name__)
api = Namespace('vehicle', description='Get available vehicles for the logged in user.')

@api.route('/')
class VehicleList(Resource):
    @flask_login.login_required
    @api.doc(responses={
        HTTPStatus.OK: 'Success',
        HTTPStatus.UNAUTHORIZED: 'Not authorized'
    })
    def get(self):
        user = flask_login.current_user
        response = requests.get(current_app.config["API_BASE"] + f"/environments/{user.environment_id}/vehicles", headers={"X-Api-Key": current_app.config["API_KEY"]})
        return response.json(), response.status_code


@api.route('/string:vehicle_id')
class VehicleSingle(Resource):
    @flask_login.login_required
    @api.doc(responses={
        HTTPStatus.OK: 'Success',
        HTTPStatus.UNAUTHORIZED: 'Not authorized'
    })
    def get(self, vehicle_id):
        user = flask_login.current_user
        response = requests.get(current_app.config["API_BASE"] + f"/vehicles/{vehicle_id}", headers={"X-Api-Key": current_app.config["API_KEY"], "vehicle_id": vehicle_id})
        return response.json(), response.status_code

import requests
import logging
from http import HTTPStatus
from flask import request, current_app
from flask_restplus import Namespace
from flask_restplus import Resource
from flask_restplus import reqparse
import flask_login


from server.models.booking import BookingModel, booking_schema, bookings_schema, booking_parser
from server.extensions.database import db

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


@api.route('/<string:vehicle_id>/bookings')
class VehicleList(Resource):
    @flask_login.login_required
    @api.doc(responses={
        HTTPStatus.OK: 'Success',
        HTTPStatus.UNAUTHORIZED: 'Not authorized'
    })
    @api.expect(booking_parser)
    def post(self, vehicle_id):
        user = flask_login.current_user
        args = booking_parser.parse_args()
        json_args = {
            "from": args["start_time"],
            "until": args["end_time"]
        }
        response = requests.post(current_app.config["API_BASE"] + f"/vehicles/{vehicle_id}/bookings", json=json_args, headers={"X-Api-Key": current_app.config["API_KEY"]})
        data = response.json()
        if response.status_code != HTTPStatus.OK:
            return data, response.status_code
        data = data["data"]
        args["start_time"] = data["from"]
        args["end_time"] = data["until"]
        args["id"] = data["id"]
        args["vehicle_id"] = vehicle_id
        args["environment_id"] = data["vehicle"]["environment"]["id"]
        args["email"] = user.email
        booking = booking_schema.load(args, session=db.session)
        db.session.add(booking)
        db.session.commit()
        return booking_schema.dump(booking), HTTPStatus.CREATED

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

import requests
import random
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
api = Namespace('booking_optimizer', description='Optimizer calculates optimal bookings.')

@api.route('/<string:vehicle_id>')
class BookingOptimizer(Resource):
    @flask_login.login_required
    @api.doc(responses={
        HTTPStatus.OK: 'Success',
        HTTPStatus.UNAUTHORIZED: 'Not authorized'
    })
    @api.expect(booking_parser)
    def get(self, vehicle_id):
        args = booking_parser.parse_args()
        args.update({"environment_id": "", "id": "", "email": "", "vehicle_id": vehicle_id})
        booking = booking_schema.load(args, session=db.session)
        bookings = BookingModel.query.filter(BookingModel.vehicle_id == vehicle_id).all()

        return self.lars_optimizer(booking, bookings, vehicle_id), HTTPStatus.OK

    def lars_optimizer(self, requested_booking, existing_bookings, vehicle_id):
        data = requests.get(current_app.config["API_BASE"] + f"/vehicles/{vehicle_id}/signals", headers={"X-Api-Key": current_app.config["API_KEY"]}).json()
        calculated_remaining_distance = data["data"]["calculated_remaining_distance"]

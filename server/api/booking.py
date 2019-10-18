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
api = Namespace('booking', description='Booking related endpoints.')

booking_patch_parser = reqparse.RequestParser()
booking_patch_parser.add_argument('id', type=str, required=True, location="json")
booking_patch_parser.add_argument('action', type=str, required=True, location="json")

@api.route('/me')
class Booking(Resource):
    @flask_login.login_required
    @api.doc(responses={
        HTTPStatus.OK: 'Success',
        HTTPStatus.UNAUTHORIZED: 'Not authorized'
    })
    def get(self):
        user = flask_login.current_user
        booking = BookingModel.query.filter(BookingModel.email == user.email).all()
        return bookings_schema.dump(booking), HTTPStatus.OK

    @flask_login.login_required
    @api.doc(responses={
        HTTPStatus.OK: 'Success',
        HTTPStatus.UNAUTHORIZED: 'Not authorized'
    })
    @api.expect(booking_patch_parser)
    def patch(self):
        args = booking_patch_parser.parse_args()
        resp = requests.patch(current_app.config["API_BASE"] + f"/bookings/{args['id']}/{args['action']}", headers={"X-Api-Key": current_app.config["API_KEY"]})
        return resp.json(), resp.status_code

@api.route('/')
class BookingList(Resource):
    @flask_login.login_required
    @api.doc(responses={
        HTTPStatus.OK: 'Success',
        HTTPStatus.UNAUTHORIZED: 'Not authorized'
    })
    def get(self):
        # get all public bookings in my environment
        user = flask_login.current_user
        bookings = BookingModel.query.filter(BookingModel.public == True, BookingModel.environment_id == user.environment_id).all()
        return bookings_schema.dump(bookings), HTTPStatus.OK

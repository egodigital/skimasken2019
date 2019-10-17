import requests
import random
import logging
from http import HTTPStatus
from flask import request
from flask_restplus import Namespace
from flask_restplus import Resource

from server.models.booking import BookingModel, booking_schema, bookings_schema, booking_parser
from server.extensions.database import db

log = logging.getLogger(__name__)
api = Namespace('booking', description='Booking related endpoints.')

@api.route('/<string:APIid>')
class Booking(Resource):
    def get(self, APIid):
        booking = BookingModel.query.filter(BookingModel.APIid == APIid).first()
        return booking_schema.dump(booking), HTTPStatus.OK

    def delete(self, APIid):
        booking = BookingModel.query.filter(BookingModel.APIid == APIid).first()
        if booking:
            db.session.delete(booking)
            db.session.commit()
        return "", HTTPStatus.NO_CONTENT

@api.route('/')
class BookingList(Resource):
    def get(self):
        return bookings_schema.dump(BookingModel.query.all()), HTTPStatus.OK

    @api.expect(booking_parser)
    def post(self):
        booking = booking_schema.load(booking_parser.parse_args(), session=db.session)
        db.session.add(booking)
        db.session.commit()
        return booking_schema.dump(booking), HTTPStatus.CREATED

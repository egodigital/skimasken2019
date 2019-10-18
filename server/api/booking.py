import requests
import random
import logging
from http import HTTPStatus
from flask import request
from flask_restplus import Namespace
from flask_restplus import Resource
import flask_login

from server.models.booking import BookingModel, booking_schema, bookings_schema, booking_parser
from server.extensions.database import db

log = logging.getLogger(__name__)
api = Namespace('booking', description='Booking related endpoints.')

def get_all_bookings():
    return requests.get(current_app.config["API_BASE"] + f"/bookings", headers={"X-Api-Key": current_app.config["API_KEY"]}).json()

@api.route('/<string:id>')
class Booking(Resource):
    def get(self, id):
        booking = BookingModel.query.filter(BookingModel.id == id).first()
        return booking_schema.dump(booking), HTTPStatus.OK

    def delete(self, id):
        booking = BookingModel.query.filter(BookingModel.id == id).first()
        if booking:
            db.session.delete(booking)
            db.session.commit()
        return "", HTTPStatus.NO_CONTENT

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

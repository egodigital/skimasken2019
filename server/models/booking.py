from datetime import datetime
from server import db
from server.extensions.marshmallow import ma
from flask_restplus import reqparse


booking_parser = reqparse.RequestParser()
booking_parser.add_argument('start_time', type=datetime, required=True, location="json")
booking_parser.add_argument('end_time', type=datetime, required=True, location="json")
booking_parser.add_argument('id', type=int, required=True, location="json")
booking_parser.add_argument('fuzzy', type=bool, required=True, location="json")
booking_parser.add_argument('car_id', type=str, required=True, location="json")
booking_parser.add_argument('duration', type=int, required=True, location="json")
booking_parser.add_argument('status', type=str, required=True, location="json")
booking_parser.add_argument('distance', type=int, required=True, location="json")


class BookingModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    fuzzy = db.Column(db.Boolean, nullable=False)
    car_id = db.Column(db.String, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String, nullable=False)
    distance = db.Column(db.Integer, nullable=False)


    def __init__(self, start_time, end_time, Fuzzy, car_id, duration, status, id, distance):

        self.start_time = start_time
        self.end_time = end_time
        self.Fuzzy = Fuzzy
        self.car_id = car_id
        self.duration = duration
        self.id = id
        self.status = status
        self.distance = distance


class BookingSchema(ma.ModelSchema):
    class Meta:
        model = BookingModel


booking_schema = BookingSchema()
bookings_schema = BookingSchema(many=True)

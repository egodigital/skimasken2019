from datetime import datetime
from server import db
from server.extensions.marshmallow import ma
from flask_restplus import reqparse


booking_parser = reqparse.RequestParser()
booking_parser.add_argument('start_time', type=datetime, required=True, location="json")
booking_parser.add_argument('end_time', type=datetime, required=True, location="json")
booking_parser.add_argument('start_time_fuzzy', type=datetime, required=False, location="json")
booking_parser.add_argument('end_time_fuzzy', type=datetime, required=False, location="json")
booking_parser.add_argument('id', type=int, required=True, location="json")
booking_parser.add_argument('fuzzy', type=bool, required=True, location="json")
booking_parser.add_argument('car_id', type=str, required=True, location="json")
booking_parser.add_argument('duration', type=int, required=True, location="json")
booking_parser.add_argument('status', type=str, required=True, location="json")

class BookingModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    fuzzy = db.Column(db.Boolean, nullable=False)
    car_id = db.Column(db.String, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    start_time_fuzzy = db.Column(db.DateTime, nullable=True)
    end_time_fuzzy = db.Column(db.DateTime, nullable=True)

    def __init__(self, start_time, end_time, Fuzzy, car_id, duration, start_time_fuzzy=None, end_time_fuzzy=None):
        self.start_time = start_time
        self.end_time = end_time
        self.Fuzzy = Fuzzy
        self.car_id = car_id
        self.duration = duration
        self.start_time_fuzzy = start_time_fuzzy
        self.end_time_fuzzy = end_time_fuzzy


class BookingSchema(ma.ModelSchema):
    class Meta:
        model = BookingModel


booking_schema = BookingSchema()
bookings_schema = BookingSchema(many=True)

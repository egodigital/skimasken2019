from server import db
from server.extensions.marshmallow import ma
from flask_restplus import reqparse


booking_parser = reqparse.RequestParser()
booking_parser.add_argument('start_time', type=str, required=True)
booking_parser.add_argument('end_time', type=str, required=True)
booking_parser.add_argument('start_time_fuzzy', type=str, required=False)
booking_parser.add_argument('end_time_fuzzy', type=str, required=False)
booking_parser.add_argument('APIid', type=str, required=True)
booking_parser.add_argument('Fuzzy', type=bool, required=True)
booking_parser.add_argument('car_id', type=str, required=True)
booking_parser.add_argument('duration', type=str, required=True)

class BookingModel(db.Model):
    APIid = db.Column(db.String, primary_key=True)
    start_time = db.Column(db.String, nullable=False)
    end_time = db.Column(db.String, nullable=False)
    Fuzzy = db.Column(db.Boolean, nullable=False)
    car_id = db.Column(db.String, nullable=False)
    duration = db.Column(db.String, nullable=False)
    start_time_fuzzy = db.Column(db.String, nullable=True)
    end_time_fuzzy = db.Column(db.String, nullable=True)

    def __init__(self, APIid, start_time, end_time, Fuzzy, car_id, duration, start_time_fuzzy=None, end_time_fuzzy=None):

        self.APIid = APIid
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

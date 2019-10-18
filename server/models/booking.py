from datetime import datetime
from server import db
from server.extensions.marshmallow import ma
from flask_restplus import reqparse

booking_parser = reqparse.RequestParser()
booking_parser.add_argument('start_time', type=str, required=True, location="json")
booking_parser.add_argument('end_time', type=str, required=True, location="json")
booking_parser.add_argument('fuzzy', type=bool, required=True, location="json")
booking_parser.add_argument('public', type=bool, required=True, location="json")
booking_parser.add_argument('distance', type=int, required=True, location="json")
booking_parser.add_argument('destination', type=str, required=True, location="json")


class BookingModel(db.Model):
    id = db.Column(db.String, primary_key=True)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    fuzzy = db.Column(db.Boolean, nullable=False)
    public = db.Column(db.Boolean, nullable=False)
    vehicle_id = db.Column(db.String, nullable=False)
    environment_id = db.Column(db.String, nullable=False)
    distance = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String, nullable=False)
    destination = db.Column(db.String, nullable=True)

    def __init__(self, id, vehicle_id, environment_id, email, start_time, end_time, fuzzy, public, distance, destination):
        self.start_time = start_time
        self.end_time = end_time
        self.fuzzy = fuzzy
        self.vehicle_id = vehicle_id
        self.id = id
        self.public = public
        self.distance = distance
        self.email = email
        self.destination = destination
        self.environment_id = environment_id

    def get_duration(self):
        return (self.end_time - self.start_time).total_seconds() // 60

    def overlaps(self, other):
        if self.start_time <= other.start_time and self.end_time > other.start_time:
            return True
        if other.start_time <= self.start_time and other.end_time > self.start_time:
            return True
        return False

    def __repr__(self):
        return f"{self.start_time}: {self.get_duration()}m"

    def __lt__(self, other):
        return self.start_time < other.start_time

class BookingSchema(ma.ModelSchema):
    class Meta:
        model = BookingModel


booking_schema = BookingSchema()
bookings_schema = BookingSchema(many=True)

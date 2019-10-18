from server import db
from server.extensions.marshmallow import ma
from flask_restplus import reqparse


experience_assignment_parser = reqparse.RequestParser()
experience_assignment_parser.add_argument('email', type=str, required=True)
experience_assignment_parser.add_argument('charger_exp', type=int, required=True)
experience_assignment_parser.add_argument('car_sharer_exp', type=int, required=True)
experience_assignment_parser.add_argument('eco_driver_exp', type=int, required=True)
experience_assignment_parser.add_argument('reliability_exp', type=int, required=True)
experience_assignment_parser.add_argument('charger_level', type=int, required=True)
experience_assignment_parser.add_argument('car_sharer_level', type=int, required=True)
experience_assignment_parser.add_argument('eco_driver_level', type=int, required=True)
experience_assignment_parser.add_argument('reliability_level', type=int, required=True)

class ExperienceModel(db.Model):
    email = db.Column(db.String, primary_key=True)#, autoincrement=True)
    charger_exp = db.Column(db.Integer, nullable=False)
    car_sharer_exp = db.Column(db.Integer, nullable=False)
    eco_driver_exp = db.Column(db.Integer, nullable=False)
    reliability_exp = db.Column(db.Integer, nullable=False)
    charger_level = db.Column(db.Integer, nullable=False)
    car_sharer_level = db.Column(db.Integer, nullable=False)
    eco_driver_level = db.Column(db.Integer, nullable=False)
    reliability_level = db.Column(db.Integer, nullable=False)

    def __init__(self, email, charger_exp, car_sharer_exp, eco_driver_exp,reliability_exp,charger_level, car_sharer_level, eco_driver_level,reliability_level):
        self.email=email
        self.charger_exp = charger_exp
        self.car_sharer_exp = car_sharer_exp
        self.eco_driver_exp = eco_driver_exp
        self.reliability_exp = reliability_exp
        self.charger_level = charger_level
        self.car_sharer_level = car_sharer_level
        self.eco_driver_level = eco_driver_level
        self.reliability_level = reliability_level
class ExperienceSchema(ma.ModelSchema):
    class Meta:
        model = ExperienceModel


experience_schema = ExperienceSchema()
experiences_schema = ExperienceSchema(many=True)


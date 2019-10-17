from server import db
from server.extensions.marshmallow import ma
from flask_restplus import reqparse


achievement_parser = reqparse.RequestParser()
achievement_parser.add_argument('achievement_id', type=int, required=False)
achievement_parser.add_argument('type', type=str, required=True)
achievement_parser.add_argument('level_req', type=str, required=False)
achievement_parser.add_argument('level_type', type=str, required=False)
achievement_parser.add_argument('score', type=int, required=True)

class AchievementModel(db.Model):
    achievement_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String, nullable=False)
    level_req = db.Column(db.String, nullable=True)
    level_type = db.Column(db.String, nullable=True)

    score = db.Column(db.Integer, nullable=False)

    def __init__(self, type, level_req, level_type, score):

        self.type = type
        self.level_req = level_req
        self.level_type = level_type
        self.score = score

class AchievementSchema(ma.ModelSchema):
    class Meta:
        model = AchievementModel

achievement_schema = AchievementSchema()
achievements_schema = AchievementSchema(many=True)


from server import db
from server.extensions.marshmallow import ma
from flask_restplus import reqparse
from server.models.user import UserModel
from server.models.achievement import AchievementModel
from server.models.user import UserModel

achievement_assignment_parser = reqparse.RequestParser()
achievement_assignment_parser.add_argument('achievement_id', type=int, required=True)
achievement_assignment_parser.add_argument('user_email', type=str, required=True)

class AchievementAssignmentModel(db.Model):
    achievement_id = db.Column(db.String, db.ForeignKey('achievement_model.achievement_id'), primary_key=True)
    user_email = db.Column(db.String, db.ForeignKey('user_model.email'), primary_key=True)

    def __init__(self, achievement_id, user_email):
        self.achievement_id = achievement_id
        self.user_email = user_email

class AchievementAssignmentSchema(ma.ModelSchema):
    class Meta:
        model = AchievementAssignmentModel

achievement_assignment_schema = AchievementAssignmentSchema()
achievements_assignment_schema = AchievementAssignmentSchema(many=True)

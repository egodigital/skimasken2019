from server import db
from server.extensions.marshmallow import ma
from flask_restplus import reqparse

achievement_assignment_parser = reqparse.RequestParser()
achievement_assignment_parser.add_argument('achievement_id', type=int, required=True)
achievement_assignment_parser.add_argument('user_email', type=str, required=True)

class AchievementAssignmentModel(db.Model):
    achievement_id = db.Column(db.Integer,  primary_key=True) #db.ForeignKey('achievement_model.achievement_id'), problem with marshmeloow
    user_email = db.Column(db.String, primary_key=True) # db.ForeignKey('user_model.email'), problems with marshmello

    def __init__(self, achievement_id, user_email):
        self.achievement_id = achievement_id
        self.user_email = user_email

class AchievementAssignmentSchema(ma.ModelSchema):
    class Meta:
        model = AchievementAssignmentModel

achievement_assignment_schema = AchievementAssignmentSchema()
achievements_assignment_schema = AchievementAssignmentSchema(many=True)

import requests
import random
import logging
from http import HTTPStatus
from flask import request
from flask_restplus import Namespace
from flask_restplus import Resource

from server.models.achievement_assignment import AchievementAssignmentModel, achievement_assignment_schema, \
    achievements_assignment_schema, achievement_assignment_parser
from server.extensions.database import db

log = logging.getLogger(__name__)
api = Namespace('achievement assignment', description='achievement assignment related endpoints.')

@api.route('/<string:achievement_id>,<string:user_email>')
class AchievementAssignment(Resource):
    def get(self, achievement_id, user_email):
        achievement_assignment = AchievementAssignmentModel.query.filter(AchievementAssignmentModel.achievement_id == achievement_id, AchievementAssignmentModel.user_email == user_email).first()
        return achievement_assignment_schema.dump(achievement_assignment), HTTPStatus.OK

    def delete(self, achievement_id, user_email):
        achievement_assignment = AchievementAssignmentModel.query.filter(AchievementAssignmentModel.achievement_id == achievement_id, AchievementAssignmentModel.user_email == user_email).first()
        if achievement_assignment:
            db.session.delete(achievement_assignment)
            db.session.commit()
        return "", HTTPStatus.NO_CONTENT

@api.route('/')
class AchievementAssignmentList(Resource):
    def get(self):
        return achievements_assignment_schema.dump(AchievementAssignmentModel.query.all()), HTTPStatus.OK

    @api.expect(achievement_assignment_parser)
    def post(self):
        achievement_assignment = achievement_assignment_schema.load(achievement_assignment_parser.parse_args(), session=db.session)
        db.session.add(achievement_assignment)
        db.session.commit()
        return achievement_assignment_schema.dump(achievement_assignment), HTTPStatus.CREATED

import requests
import random
import logging
from http import HTTPStatus
from flask import request
from flask_restplus import Namespace
from flask_restplus import Resource

from server.models.achievement import AchievementModel, achievement_schema, achievement_parser
from server.extensions.database import db

log = logging.getLogger(__name__)
api = Namespace('achievement', description='achievement related endpoints.')

@api.route('/<string:email>')
class achievement(Resource):
    def get(self, achievement_id):
        achievement = AchievementModel.query.filter(AchievementModel.achievement_id == achievement_id).first()
        return achievement_schema.dump(achievement), HTTPStatus.OK

    def delete(self, achievement_id):
        user = AchievementModel.query.filter(AchievementModel.email == email).first()
        if user:
            db.session.delete(user)
            db.session.commit()
        return "", HTTPStatus.NO_CONTENT

@api.route('/')
class UserList(Resource):
    def get(self):
        return achievement_schema.dump(AchievementModel.query.all()), HTTPStatus.OK

    @api.expect(achievement_parser)
    def post(self):
        user = achievement_schema.load(achievement_parser.parse_args(), session=db.session)
        db.session.add(user)
        db.session.commit()
        return achievement_schema.dump(user), HTTPStatus.CREATED

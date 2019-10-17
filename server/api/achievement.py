import requests
import random
import logging
from http import HTTPStatus
from flask import request
from flask_restplus import Namespace
from flask_restplus import Resource

from server.models.achievement import AchievementModel, achievement_schema,achievements_schema, achievement_parser
from server.extensions.database import db

log = logging.getLogger(__name__)
api = Namespace('achievement', description='achievement related endpoints.')

@api.route('/<string:achievement_id>')
class achievement(Resource):
    def get(self, achievement_id):
        achievement = AchievementModel.query.filter(AchievementModel.achievement_id == achievement_id).first()
        return achievement_schema.dump(achievement), HTTPStatus.OK

    def delete(self, achievement_id):
        achievement = AchievementModel.query.filter(AchievementModel.achievement_id == achievement_id).first()
        if achievement:
            db.session.delete(achievement)
            db.session.commit()
        return "", HTTPStatus.NO_CONTENT

@api.route('/')
class AchievementList(Resource):
    def get(self):
        return achievements_schema.dump(AchievementModel.query.all()), HTTPStatus.OK

    @api.expect(achievement_parser)
    def post(self):
        achievement = achievement_schema.load(achievement_parser.parse_args(), session=db.session)
        db.session.add(achievement)
        db.session.commit()
        return achievement_schema.dump(achievement), HTTPStatus.CREATED

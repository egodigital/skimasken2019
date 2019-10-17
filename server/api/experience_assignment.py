import requests
import random
import logging
from http import HTTPStatus
from flask import request
from flask_restplus import Namespace
from flask_restplus import Resource

from server.models.experience_assignment import ExperienceModel, experience_schema,experiences_schema, experience_assignment_parser
from server.extensions.database import db

log = logging.getLogger(__name__)
api = Namespace('experience assignment', description='Experience assignment related endpoints.')

@api.route('/<string:email>')
class Experience(Resource):
    def get(self, email):
        experience = ExperienceModel.query.filter(ExperienceModel.email == email).first()
        return experience_schema.dump(experience), HTTPStatus.OK

    def delete(self, email):
        achievement = ExperienceModel.query.filter(ExperienceModel.email == email).first()
        if achievement:
            db.session.delete(achievement)
            db.session.commit()
        return "", HTTPStatus.NO_CONTENT

@api.route('/')
class ExperienceList(Resource):
    def get(self):
        return experiences_schema.dump(ExperienceModel.query.all()), HTTPStatus.OK

    @api.expect(experience_assignment_parser)
    def post(self):
        experience = experience_schema.load(experience_assignment_parser.parse_args(), session=db.session)
        db.session.add(experience)
        db.session.commit()
        return experience_schema.dump(experience), HTTPStatus.CREATED

from server import db
from server.extensions.marshmallow import ma
from flask_restplus import reqparse

user_parser = reqparse.RequestParser()
user_parser.add_argument('email', type=str, required=True)
user_parser.add_argument('name', type=str, required=True)
user_parser.add_argument('password', type=str, required=True)
user_parser.add_argument('user_name', type=str, required=True)
user_parser.add_argument('environment_id', type=str, required=True)


class UserModel(db.Model):
    email = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    user_name = db.Column(db.String, nullable=False)

    environment_id = db.Column(db.String, nullable=False)

    def __init__(self, email, name, password, user_name, environment_id):
        self.email = email
        self.name = name
        self.password = password
        self.user_name = user_name
        self.environment_id = environment_id

class UserSchema(ma.ModelSchema):
    class Meta:
        model = UserModel

user_schema = UserSchema()
users_schema = UserSchema(many=True)

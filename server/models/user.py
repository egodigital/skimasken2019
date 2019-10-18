from server import db
from server.extensions.marshmallow import ma
from flask_restplus import reqparse
from werkzeug import security

user_parser = reqparse.RequestParser()
user_parser.add_argument('email', type=str, required=True, location="json")
user_parser.add_argument('name', type=str, required=True, location="json")
user_parser.add_argument('password', type=str, required=True, location="json")
user_parser.add_argument('user_name', type=str, required=True, location="json")
user_parser.add_argument('environment_id', type=str, required=True, location="json")


class UserModel(db.Model):
    is_authenticated = db.Column(db.Boolean, nullable=False)
    email = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    user_name = db.Column(db.String, nullable=False)

    environment_id = db.Column(db.String, nullable=False)

    def __init__(self, email, name, password, user_name, environment_id):
        self.is_authenticated = False
        self.email = email
        self.name = name
        self.password = security.generate_password_hash(password)
        self.user_name = user_name
        self.environment_id = environment_id

    def check_password(password):
        return security.check_password_hash(self.password, password)

    def is_authenticated(self):
        return self.is_authenticated
 
    def is_active(self):
        return True
 
    def is_anonymous(self):
        return False
 
    def get_id(self):
        return self.email

class UserSchema(ma.ModelSchema):
    class Meta:
        model = UserModel

user_schema = UserSchema(load_only=("password", ))
users_schema = UserSchema(load_only=("password", ), many=True)

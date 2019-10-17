from flask_restplus import Api

from .user import api as ns1
from .achievement import api as ns2

api = Api(
    title='eGOn API',
    version='1.0',
    description='Work in progress.'
)

api.add_namespace(ns1, path='/api/user')
api.add_namespace(ns2, path='/api/achievement')

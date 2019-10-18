from flask_restplus import Api

from .user import api as ns1
from .booking import api as ns2
from .achievement import api as ns3
from .achievement_assignment import api as ns4
from .experience_assignment import api as ns5
from .vehicle import api as ns6
from .environment import api as ns7
from .booking_optimizer import api as ns8

api = Api(
    title='eGOn API',
    version='1.0',
    description='Work in progress.'
)

api.add_namespace(ns1, path='/api/user')
api.add_namespace(ns2, path='/api/booking')
api.add_namespace(ns3, path='/api/achievement')
api.add_namespace(ns4, path='/api/achievement_assignment')
api.add_namespace(ns5, path='/api/experience_assignment')
api.add_namespace(ns6, path='/api/vehicle')
api.add_namespace(ns7, path='/api/environment')
api.add_namespace(ns8, path='/api/booking/optimizer')


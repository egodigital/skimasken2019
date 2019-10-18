class DefaultConfig:
    CONFIG_NAME = "DefaultConfig"
    LOGGING_CONFIG = "logging.conf"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///egon.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    TESTING = False
    PORT = 3000
    SECRET_KEY = "Tg36Otbt8OhNrZESWaV,])YA{vg00q?Q'[ng4hz43z43z4s],TCp3RSNwo5rp:OiE1b'GY[<tz"
    API_KEY = "0920e794-950a-475b-bfa0-f4d5355c51e6"
    API_BASE = "https://ego-vehicle-api.azurewebsites.net/api/v2"


class DevConfig(DefaultConfig):
    CONFIG_NAME = "DevConfig"
    TESTING = True
    DEBUG = True

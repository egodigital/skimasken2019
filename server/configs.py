class DefaultConfig:
    CONFIG_NAME = "DefaultConfig"
    LOGGING_CONFIG = "logging.conf"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///egon.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    TESTING = False
    PORT = 5000


class DevConfig(DefaultConfig):
    CONFIG_NAME = "DevConfig"
    TESTING = True
    DEBUG = True

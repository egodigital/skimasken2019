from server import create_app
from server.configs import DevConfig

if __name__ == '__main__':
    app = create_app(DevConfig)
    app.run(port=DevConfig.PORT)
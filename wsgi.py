from server import create_app
from server.configs import DevConfig

app = create_app(DevConfig)

if __name__ == '__main__':
    app.run(port=DevConfig.PORT)
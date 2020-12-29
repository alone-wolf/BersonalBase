import os


class DBConfig:
    def __init__(self):
        self.SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.abspath(".") + "/data.db"
        self.SQLALCHEMY_TRACK_MODIFICATIONS = False


class AdminConfig:
    def __init__(self):
        self.FLASK_ADMIN_SWATCH = 'cerulean'


def init_config(item, server_app):
    for k, v in item.__dict__.items():
        server_app.config[k] = v
    return server_app


def init_configure(server_app):
    server_app = init_config(DBConfig(), server_app)
    server_app = init_config(AdminConfig(), server_app)
    return server_app

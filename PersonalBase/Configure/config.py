import os


class DBConfig:
    def __init__(self):
        DATABASE_PATH = "{}/data".format(os.getcwd())
        if not (os.path.exists(DATABASE_PATH) and os.path.isdir(DATABASE_PATH)):
            os.mkdir(DATABASE_PATH)
        self.SQLALCHEMY_DATABASE_URI = "sqlite:///{}/data.db".format(DATABASE_PATH)
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

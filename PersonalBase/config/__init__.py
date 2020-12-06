from PersonalBase.config.error import init_error_page
from PersonalBase.config.setting import Setting


def init_config(server):
    server.config['SQLALCHEMY_DATABASE_URI'] = Setting.SQLALCHEMY_DATABASE_URI
    server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Setting.SQLALCHEMY_TRACK_MODIFICATIONS

    init_error_page(server)

    return server

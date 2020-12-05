from PersonalBase.apps.Notify.routes import Notify_routes


def init_app_notify(server):
    server.register_blueprint(Notify_routes)
    return server

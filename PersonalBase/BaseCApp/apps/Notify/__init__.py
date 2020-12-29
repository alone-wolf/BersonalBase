from PersonalBase.BaseCApp.apps.Notify.routes import init_notify_blueprint


class AppSection:
    name = "Notify"
    ServerApp = None
    blueprint = None
    db = None
    admin = None

    def __init__(self, server_app, db, admin_):
        self.ServerApp = server_app
        self.db = db
        self.admin = admin_

    def set_admin(self):
        pass

    def set_blueprint(self):
        self.blueprint = init_notify_blueprint()
        self.ServerApp.register_blueprint(self.blueprint)

    def set_socket_io(self):
        pass

import os

from flask import Flask
from flask_admin import Admin
from flask_socketio import SocketIO

from PersonalBase.Configure import init_configure
from PersonalBase.BaseCApp.Alchemy import init_sqlalchemy
from PersonalBase.BaseCApp.apps import init_apps
from PersonalBase.BaseCApp.ErrorPage import init_error_page
from PersonalBase.BaseCApp.Hooks import init_hooks_main
from PersonalBase.BaseCApp.SocketIO import init_socket_io_main


class Base0App:
    alchemy = None
    admin = None
    apps = []
    socket_io = None

    def __init__(self, template_folder='templates', static_folder="static"):
        self.server_app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
        init_error_page(self.server_app)
        self.init_server()

        self.init_app()
        self.init_app_admin()
        self.init_app_routes()
        self.init_app_socket_io()

    def init_server(self):
        init_configure(self.server_app)
        self.alchemy = init_sqlalchemy(self.server_app)
        self.admin = Admin(self.server_app, name='ok', template_mode='bootstrap3')
        self.socket_io = init_socket_io_main(self.server_app)
        init_hooks_main(self.server_app, self.alchemy)

    def init_app(self):
        self.apps = [(i.name, i) for i in init_apps(self.server_app, self.alchemy, self.admin)]

    def init_app_admin(self):
        for _, app in self.apps:
            app.set_admin()

    def init_app_routes(self):
        for _, app in self.apps:
            app.set_blueprint()

    def init_app_socket_io(self):
        for _, app in self.apps:
            app.set_socket_io()

    def run(self):
        if self.socket_io is not None:
            print(" * running on SocketIO")
            self.socket_io.run(self.server_app, debug=True)
        else:
            print(" * running on Flask ServerApp")
            self.server_app.run(debug=True)


if __name__ == '__main__':
    print(os.path.abspath("."))
    b = Base0App("../templates", "../static")
    b.run()

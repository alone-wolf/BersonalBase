from PersonalBase.apps.Tab.routes import Tab_routes


def init_app_tab(server):
    server.register_blueprint(Tab_routes)
    return server

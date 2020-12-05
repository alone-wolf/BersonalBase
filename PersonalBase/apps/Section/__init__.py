from PersonalBase.apps.Section.routes import Section_routes


def init_app_section(server):
    server.register_blueprint(Section_routes)
    return server

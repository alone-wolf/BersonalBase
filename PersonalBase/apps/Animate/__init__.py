from PersonalBase.apps.Animate.routes import Animate_routes


def init_app_animate(server):
    server.register_blueprint(Animate_routes)
    return server

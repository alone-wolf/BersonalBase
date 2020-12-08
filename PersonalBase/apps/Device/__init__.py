from PersonalBase.apps.Device.routes import Device_routes


def init_app_device(server):
    server.register_blueprint(Device_routes)
    return server

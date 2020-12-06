from flask_socketio import SocketIO, emit

from PersonalBase.apps.Animate import init_app_animate
from PersonalBase.apps.Door import init_app_door
from PersonalBase.apps.Notify import init_app_notify
from PersonalBase.apps.R import init_app_r
from PersonalBase.apps.Section import init_app_section


def init_apps(server):
    init_app_door(server)
    init_app_r(server)
    init_app_section(server)
    init_app_animate(server)
    init_app_notify(server)
    return server

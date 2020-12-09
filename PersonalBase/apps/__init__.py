from PersonalBase.apps.Animate import init_app_animate
from PersonalBase.apps.Device import init_app_device
from PersonalBase.apps.Door import init_app_door
from PersonalBase.apps.Notify import init_app_notify
from PersonalBase.apps.R import init_app_r
from PersonalBase.apps.Section import init_app_section
from PersonalBase.apps.Tab import init_app_tab


def init_apps(server):
    init_app_door(server)
    init_app_r(server)
    init_app_section(server)
    init_app_animate(server)
    init_app_notify(server)
    init_app_device(server)
    init_app_tab(server)
    return server

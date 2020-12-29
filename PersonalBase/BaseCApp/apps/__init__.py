from PersonalBase.BaseCApp.apps.Section import AppSection as SectionNode
from PersonalBase.BaseCApp.apps.Notify import AppSection as NotifyNode
from PersonalBase.BaseCApp.apps.Animate import AppSection as AnimateNode


def init_apps(server_app, db, admin):
    return \
        SectionNode(server_app, db, admin), \
        NotifyNode(server_app, db, admin), \
        AnimateNode(server_app, db, admin),

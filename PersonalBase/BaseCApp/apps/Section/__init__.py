from PersonalBase.BaseCApp.apps.Section.admin import SectionView
# from PersonalBase.BaseCApp.apps.Section.func import Func
from PersonalBase.BaseCApp.apps.Section.model import Section
from PersonalBase.BaseCApp.apps.Section.routes import init_section_blueprint


class AppSection:
    name = "Section"
    ServerApp = None
    blueprint = None
    db = None
    admin = None
    # model = None

    def __init__(self, server_app, db, admin_):
        self.ServerApp = server_app
        self.db = db
        self.admin = admin_
        # self.set_model()
        # self.set_admin()
        # self.set_blueprint()

    # def set_model(self):
    #     self.Model = init_model(self.db)

    def set_admin(self):
        self.admin.add_view(SectionView(Section, self.db.session))

    def set_blueprint(self):
        self.blueprint = init_section_blueprint()
        self.ServerApp.register_blueprint(self.blueprint)

    def set_socket_io(self):
        pass

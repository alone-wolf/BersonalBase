from flask_admin import Admin

from PersonalBase.apps.Door.admin import admin_add_door
from PersonalBase.apps.R.admin import admin_add_r
from PersonalBase.apps.Section.admin import admin_add_section


def init_admin(server):
    server.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(server, name='ok', template_mode='bootstrap3')
    admin_add_section(admin)
    admin_add_door(admin)
    admin_add_r(admin)
    return server

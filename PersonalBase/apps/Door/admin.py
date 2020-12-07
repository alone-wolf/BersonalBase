from flask_admin.contrib.sqla import ModelView

from PersonalBase.apps.Door.models import Door
from PersonalBase.common.ext import db


def admin_add_door(admin):
    admin.add_view(ModelView(Door, db.session))
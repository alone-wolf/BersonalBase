from flask_admin.contrib.sqla import ModelView

from PersonalBase.apps.Section.models import Section
from PersonalBase.common.ext import db


def admin_add_section(admin):
    admin.add_view(ModelView(Section, db.session))
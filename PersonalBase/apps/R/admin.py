from flask_admin.contrib.sqla import ModelView

from PersonalBase.apps.R.models import R
from PersonalBase.common.SQLAlchemy import db


def admin_add_r(admin):
    admin.add_view(ModelView(R, db.session))

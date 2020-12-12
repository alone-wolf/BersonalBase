from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.sqla.filters import FilterEqual

from PersonalBase.apps.Section.models import Section
from PersonalBase.common.SQLAlchemy import db


class SectionView(ModelView):
    can_create = False
    can_delete = False
    can_export = True
    can_view_details = True
    column_filters = (
        FilterEqual(
            Section.function,
            "Function",
            options=[
                ["notify", "Notify"], ["animeEpisode", "AnimeEpisode"]
            ]),
        FilterEqual(
            Section.function,
            "Type",
            options=[
                ["json", "Json"], ["rawText", "RawText"]
            ]),
    )


def admin_add_section(admin):
    admin.add_view(SectionView(Section, db.session))

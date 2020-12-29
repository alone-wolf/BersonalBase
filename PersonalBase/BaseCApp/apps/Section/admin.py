from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.sqla.filters import FilterEqual

from PersonalBase.BaseCApp.apps.Section.model import Section


class SectionView(ModelView):
    # can_create = False
    can_delete = False
    can_export = True
    can_view_details = True

    column_filters = (
        FilterEqual(
            Section.function,
            "Function",
            options=[
                ["notify", "Notify"], ["animeEpisode", "AnimeEpisode"], ["device", "Device"]
            ]),
        FilterEqual(
            Section.function,
            "Type",
            options=[
                ["json", "Json"], ["rawText", "RawText"]
            ]),
    )

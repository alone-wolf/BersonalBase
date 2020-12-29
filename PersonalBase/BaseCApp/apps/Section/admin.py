from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.sqla.filters import FilterEqual


class SectionView(ModelView):
    # can_create = False
    can_delete = False
    can_export = True
    can_view_details = True

    def __init__(self, model, session):
        super().__init__(model, session)
        self.model = model
        self.column_filters = (
            FilterEqual(
                model.function,
                "Function",
                options=[
                    ["notify", "Notify"], ["animeEpisode", "AnimeEpisode"], ["device", "Device"]
                ]),
            FilterEqual(
                model.function,
                "Type",
                options=[
                    ["json", "Json"], ["rawText", "RawText"]
                ]),
        )

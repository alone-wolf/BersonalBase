class Setting:
    ACCESS_TOKEN_KEY = "access_token"
    ACCESS_TOKEN_VALUE = "asdfghjkl"
    ENABLE_ACCESS_TOKEN_CHECK = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///../data/data.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DoorIsOpen = False

    class WebSocket:
        ROOT_NAMESPACE = "/root_ns"

    class Section:
        class Function:
            UnDefined = "undefined"
            Notify = "notify"
            Task = "task"
            AnimeEpisode = "animeEpisode"
            Share = "share"
            Device = "device"
            Tab = "tab"
            List = [UnDefined, Notify, Task, AnimeEpisode, Share, Device, Tab]

        class Type:
            RawText = "rawText"
            Json = "json"
            Ini = "ini"
            UrlStr = "url"
            List = [RawText, Json, Ini, UrlStr]

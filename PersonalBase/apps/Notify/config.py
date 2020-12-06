from PersonalBase.config import Setting


class Config:
    Function = "notify"
    Type = "json"

    class WebSocket:
        NAMESPACE = Setting.WebSocket.ROOT_NAMESPACE

        ROOM = "room_notify"

        ENTRANCE_NOTIFY = "en_notify"
        ENTRANCE_NOTIFY_MONITOR_ONLY = "en_notify_monitor_only"

        SEND_TYPE_ALL = "all"
        SEND_TYPE_MONITOR_ONLY = "monitor_only"

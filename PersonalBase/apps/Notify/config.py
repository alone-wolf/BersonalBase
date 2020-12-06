class Config:
    Function = "notify"
    Type = "json"

    class WebSocket:
        NAMESPACE = "/notify"

        ENTRANCE_NOTIFY = "notify"
        ENTRANCE_NOTIFY_MONITOR_ONLY = "notify_monitor_only"

        SEND_TYPE_ALL = "all"
        SEND_TYPE_MONITOR_ONLY = "monitor_only"

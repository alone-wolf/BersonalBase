from PersonalBase.config import Setting


class Config:
    Function = "device"
    Type = "json"

    class DevicePlatform:
        Apple = "apple"
        Android = "android"
        Windows = "windows"
        Linux = "linux"
        BSD = "bsd"
        Web = "web"
        Other = "other"

    class WebSocket:
        NAMESPACE = Setting.WebSocket.ROOT_NAMESPACE

        ENTRANCE_DEVICE = "en_device"

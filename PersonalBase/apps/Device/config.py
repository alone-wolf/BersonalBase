from PersonalBase.apps.Notify.config import Config
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
        PlatformList = (Apple, Android, Windows, Linux, BSD, Web, Other)

    class DevicePower:
        Battery = "battery"
        AC = "ac"
        DC = "dc"
        Unknown = "unknown"
        PowerList = (Battery, AC, DC, Unknown)

    class WebSocket:
        NAMESPACE = Setting.WebSocket.ROOT_NAMESPACE

        ENTRANCE_DEVICE = "en_device"

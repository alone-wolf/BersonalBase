from PersonalBase.Configure import Setting
from PersonalBase.Configure.section_config import SectionConfig


class Config:
    Function = SectionConfig.Function.Notify
    Type = SectionConfig.Type.Json

    class WebSocket:
        NAMESPACE = Setting.SocketIO.ROOT_NAMESPACE

        # 客户端on en_xx emit(ev_xx)
        # 服务端on ev_xx emit(en_xx)
        # ENTRANCE_NOTIFY = "en_notify"
        # ENTRANCE_NOTIFY_MONITOR_ONLY = "en_notify_monitor_only"
        #
        # 服务器
        # EVENT_NOTIFY_ALL = "ev_notify_all"
        # EVENT_NOTIFY_MONITOR_ONLY = "ev_notify_monitor_only"

        class EventEntrance:
            NotifyAll = ""
            NotifyMonitorOnly = ""
            List = []

            def __init__(self, prefix="ev"):
                self.NotifyAll = "{}_notify_all".format(prefix)
                self.NotifyMonitorOnly = "{}_notify_monitor_only".format(prefix)
                self.List = list(self.__dict__.keys())

        EVENT = EventEntrance("ev")
        ENTRANCE = EventEntrance("en")


if __name__ == '__main__':
    Config.WebSocket()

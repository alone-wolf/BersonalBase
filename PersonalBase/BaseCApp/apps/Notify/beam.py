import json


class NotifyCon:

    def __init__(self, notify, title, device, time_=""):
        self.notify = notify
        self.title = title
        self.device = device
        self.time = time_

    def to_object(self):
        return self.__dict__


if __name__ == '__main__':
    n = NotifyCon("n", "t", "d").to_object()
    print(json.dumps(n))
    # print(n)

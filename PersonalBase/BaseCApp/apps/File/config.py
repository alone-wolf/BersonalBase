import os


class Config:
    Function = "file"
    Type = "json"

    class FileConfig:
        def __init__(self):
            paths = [os.getcwd(), "/data", "/files"]
            p = ""
            for i in paths:
                p += i
                if not (os.path.exists(p) and os.path.isdir(p)):
                    os.mkdir(p)
            self.StorePath = "{}/data/files".format(os.getcwd())

    FilePathConfig = FileConfig()

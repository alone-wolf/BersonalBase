from PersonalBase.Utils.dataBeam import AppBaseConfigBase


class SectionContainFunctions(AppBaseConfigBase):
    def __init__(self):
        self.Section = "section"
        self.Task = "task"
        self.Animate = "animate"
        self.Other = 'other'
        self.List = list(self.__dict__.values())


class SectionContainType(AppBaseConfigBase):
    def __init__(self):
        self.RawText = "rawText"
        self.Json = "json"
        self.Other = 'other'
        self.List = list(self.__dict__.values())


class SectionConfig:
    Function = SectionContainFunctions()
    Type = SectionContainType()


if __name__ == '__main__':
    print(SectionConfig.Function.List)
    print(SectionConfig.Type.List)

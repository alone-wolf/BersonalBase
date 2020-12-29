class DataBody:
    StatusCode: int
    Body: []
    Message: str

    def to_object(self):
        return self.__dict__
        # return {
        #     "StatusCode": self.StatusCode,
        #     "Body": self.Body,
        #     "Message": self.Message
        # }


class AppBaseConfigBase:
    Other = 'other'
    List = (Other,)

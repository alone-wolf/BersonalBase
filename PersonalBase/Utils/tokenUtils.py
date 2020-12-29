from PersonalBase.Utils.encryptUtils import get_md5
from PersonalBase.Utils.timeUtils import get_unix_time_stamp


def gen_token(a):
    return get_md5(a)


def gen_token_by_time():
    return get_md5(get_unix_time_stamp())

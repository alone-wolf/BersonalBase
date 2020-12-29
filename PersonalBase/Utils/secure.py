from functools import wraps

from flask import request, abort

# from PersonalBase.globalConfig.setting import Setting
from hmac import compare_digest


def check_access_token(func: callable, Setting=None):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if Setting is None:
            return func(*args, **kwargs)
        token = str(request.headers.get("access_token", "none"))
        if Setting.ENABLE_ACCESS_TOKEN_CHECK:
            if not compare_digest(token, "asdfghjkl"):
                return abort(401)
        return func(*args, **kwargs)

    return wrapper


def check_token(token):
    pass

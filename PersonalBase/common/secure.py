from functools import wraps

from flask import request, abort

from PersonalBase.config.setting import Setting
from hmac import compare_digest


def check_access_token(func: callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = str(request.headers.get(Setting.ACCESS_TOKEN_KEY, "none"))
        if Setting.ENABLE_ACCESS_TOKEN_CHECK:
            if not compare_digest(token, Setting.ACCESS_TOKEN_VALUE):
                return abort(401)
        return func(*args, **kwargs)

    return wrapper

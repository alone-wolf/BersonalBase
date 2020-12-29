from PersonalBase.Utils.dataBeam import AppBaseConfigBase
from flask import abort


def get_standard_request_value(form_args, standard, name, or_=None, or_abort=400):
    tmp = form_args.get(name) or or_ or abort(or_abort)
    if standard in (False, None, 0, "0", object):
        return tmp
    if issubclass(standard, AppBaseConfigBase):
        if tmp not in standard.List:
            tmp = standard.Other
        return tmp
    else:
        return tmp

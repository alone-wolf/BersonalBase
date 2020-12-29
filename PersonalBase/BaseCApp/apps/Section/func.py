import json

from PersonalBase.BaseCApp.apps.Section.sectionConfig import SectionConfig
from PersonalBase.Utils.dataBeam import DataBody
from PersonalBase.BaseCApp.apps.Section.model import Section
from flask import abort


def fun_section_get_all():
    ss = Section.db_select_all()
    b = DataBody()
    b.Body = []
    b.StatusCode = 200
    b.Message = "done"
    for i in ss:
        b.Body.append(
            {
                "id": i.id,
                "con": i.con,
                "create_time": i.create_time,
                "last_modify_time": i.last_modify_time,
                "token": i.token,
                "function": i.function,
                "type": i.type_
            }
        )
    return b.to_object()


def func_section_get_id(id_):
    i = Section.db_select_id(id_)
    if i is None:
        abort(404)
    b = DataBody()
    b.Body = {
        "id": i.id,
        "con": i.con,
        "create_time": i.create_time,
        "last_modify_time": i.last_modify_time,
        "token": i.token,
        "function": i.function,
        "type": i.type_
    }
    b.StatusCode = 200
    b.Message = "done"
    return b.to_object()


def func_section_get_function(function):
    tmp = Section.db_select_function(function)
    b = DataBody()
    b.StatusCode = 200
    b.Body = []
    b.Message = "get all animate done"
    for i in tmp:
        b.Body.append({
            "con": i.con,
            "id": i.id,
            "create_time": i.create_time,
            "last_modify_time": i.last_modify_time,
            "function": i.function,
            "type": i.type_,
            "token": i.token
        })
    return b.to_object()


def func_section_get_token(token):
    return Section.db_select_token(token)


def func_section_get_function_with_json_con(function):
    tmp = Section.db_select_function(function)
    b = DataBody()
    b.StatusCode = 200
    b.Body = []
    b.Message = "get all {} done".format(function)
    for i in tmp:
        try:
            tmp = json.loads(i.con)
        except Exception as err:
            print(err.__str__())
            tmp = {}
            pass
        b.Body.append({
            "con": tmp,
            "id": i.id,
            "create_time": i.create_time,
            "last_modify_time": i.last_modify_time,
            "function": i.function,
            "type": i.type_,
            "token": i.token
        })
    return b.to_object()


def func_section_get_function_with_json_con_thin(function):
    tmp = Section.db_select_function(function)
    b = DataBody()
    b.StatusCode = 200
    b.Body = []
    b.Message = "get all {} thin done".format(function)
    for i in tmp:
        try:
            tmp = json.loads(i.con)
        except Exception as err:
            tmp = {}
            pass
        b.Body.append(tmp)
    return b.to_object(), 200


def func_section_add(function, type_, con):
    token = Section.db_insert(con, function, type_)
    b = DataBody()
    b.Body = token
    b.Message = "new section add done"
    b.StatusCode = 200
    return b.to_object()


def func_section_modify(id_, function, type_, con):
    if (function is not None) and (function not in SectionConfig.Function.List):
        function = None
    if (type_ is not None) and (type_ not in SectionConfig.Type.List):
        type_ = None
    Section.db_update_id(id_, con, function, type_)
    b = DataBody()
    b.Body = []
    b.StatusCode = 200
    b.Message = "section modify done"
    return b.to_object()


def func_section_delete_id(id_: int, function=None, type_=None):
    if function and type_ and (function in SectionConfig.Function.List) and (type_ in SectionConfig.Type.List):
        Section.db_delete_id_check_function_type_(id_, function, type_)
    else:
        Section.db_delete_id(id_)
    b = DataBody()
    b.Body = []
    b.StatusCode = 200
    b.Message = "section delete done"
    return b.to_object()


def func_section_delete_all_function(function):
    if function not in SectionConfig.Function.List:
        return -1
    Section.db_delete_ids([i.id for i in Section.db_select_function(function)])
    return None


def func_delete_id(id_):
    Section.db_delete_id(id_)


def func_update_id(id_: int, con, function, type_):
    Section.db_update_id(id_, con, function, type_)


def func_select_id(id_):
    return Section.db_select_id(id_)

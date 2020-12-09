import json

from PersonalBase.apps.Section.models import db_select_all, db_select_id, db_insert, db_update_id, db_delete_id, \
    db_select_function
from PersonalBase.apps.Section.utils import DataBody

from flask import abort

from PersonalBase.config import Setting


class Func:
    @staticmethod
    def fun_section_get_all():
        ss = db_select_all()
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

    @staticmethod
    def func_section_get_id(id_):
        i = db_select_id(id_)
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

    @staticmethod
    def func_section_get_function(function):
        tmp = db_select_function(function)
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

    @staticmethod
    def func_section_get_function_with_json_con(function):
        tmp = db_select_function(function)
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

    @staticmethod
    def func_section_get_function_with_json_con_thin(function):
        tmp = db_select_function(function)
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

    @staticmethod
    def func_section_add(function, type_, con):
        if function not in Setting.Section.Function.List:
            function = Setting.Section.Function.UnDefined
        if type_ not in Setting.Section.Type.List:
            type_ = Setting.Section.Type.RawText
        db_insert(con, function, type_)
        b = DataBody()
        b.Body = []
        b.Message = "new section add done"
        b.StatusCode = 200
        return b.to_object()

    @staticmethod
    def func_section_modify(id_, function, type_, con):
        if (function is not None) and (function not in Setting.Section.Function.List):
            function = None
        if (type_ is not None) and (type_ not in Setting.Section.Type.List):
            type_ = None
        db_update_id(id_, con, function, type_)
        b = DataBody()
        b.Body = []
        b.StatusCode = 200
        b.Message = "section modify done"
        return b.to_object()

    @staticmethod
    def func_section_delete_id(id_):
        try:
            id_ = int(id_)
        except Exception as err:
            print(err)
        db_delete_id(id_)
        b = DataBody()
        b.Body = []
        b.StatusCode = 200
        b.Message = "section delete done"
        return b.to_object()

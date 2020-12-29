from PersonalBase.Utils.timeUtils import get_unix_time_stamp
from PersonalBase.Utils.tokenUtils import gen_token
from PersonalBase.BaseCApp.Alchemy import sqlalchemy as db


# def init_model(db):
#

class Section(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True, index=True)
    create_time = db.Column(db.String(13))
    last_modify_time = db.Column(db.String(13))
    con = db.Column(db.Text)
    function = db.Column(db.String(10))
    type_ = db.Column(db.String(10))
    token = db.Column(db.String(32), unique=True, index=True)

    @staticmethod
    def db_insert(con: str, function: str, type_: str):
        s = Section()
        s.create_time = get_unix_time_stamp()
        s.token = gen_token(s.create_time)
        s.last_modify_time = s.create_time
        s.con = con
        s.function = function
        s.type_ = type_
        db.session.add(s)
        db.session.commit()
        return s.token

    @staticmethod
    def db_insert_multi(cons: list, function: str, type_: str):
        for con in cons:
            s = Section()
            s.create_time = get_unix_time_stamp()
            s.last_modify_time = s.create_time
            s.con = str(con)
            s.function = function
            s.type_ = type_
            db.session.add(s)
        db.session.commit()

    @staticmethod
    def db_select_all():
        tmp = Section.query.all()
        return tmp

    @staticmethod
    def db_select_id(id_: int):
        tmp = Section.query.filter_by(id=id_).first()
        return tmp

    @staticmethod
    def db_select_token(token: str):
        tmp = Section.query.filter_by(token=token).first()
        return tmp

    @staticmethod
    def db_select_function(function_: str):
        function_ = str(function_)
        tmp = Section.query.filter_by(function=function_).all()
        return tmp

    @staticmethod
    def db_update_id(id_: int, con, function, type_):
        id_ = int(id_)
        tmp = Section.db_select_id(id_)
        if con:
            tmp.con = str(con)
        if function:
            tmp.function = str(function)
        if type_:
            tmp.type_ = str(type_)
        tmp.last_modify_time = get_unix_time_stamp()
        db.session.commit()

    @staticmethod
    def db_delete_id(id_: int):
        tmp = Section.db_select_id(id_)
        if tmp:
            db.session.delete(tmp)
            db.session.commit()

    @staticmethod
    def db_delete_token(token: str):
        tmp = Section.db_select_token(token)
        if tmp:
            db.session.delete(tmp)
            db.session.commit()

    @staticmethod
    def db_delete_id_check_function_type_(id_: int, function: str, type_: str):
        tmp = Section.db_select_id(id_)
        if tmp and (tmp.function == function) and (tmp.type_ == type_):
            db.session.delete(tmp)
            db.session.commit()

    @staticmethod
    def db_delete_token_check_function_type_(token: str, function: str, type_: str):
        tmp = Section.db_select_token(token)
        if tmp and (tmp.function == function) and (tmp.type_ == type_):
            db.session.delete(tmp)
            db.session.commit()

    @staticmethod
    def db_delete_ids(ids: list):
        if type(ids) is not list:
            return
        for i in ids:
            tmp = Section.db_select_id(i)
            db.session.delete(tmp)
        db.session.commit()

    @staticmethod
    def db_delete_tokens(tokens: list):
        if type(tokens) is not list:
            return
        for i in tokens:
            tmp = Section.db_select_token(i)
            db.session.delete(tmp)
        db.session.commit()

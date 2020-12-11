from flask import Blueprint, render_template, request, abort

from PersonalBase.apps.Section.route_func import Func
from PersonalBase.common.secure import check_access_token
from PersonalBase.config import Setting
from PersonalBase.config.error import StatusCode

Section_routes = Blueprint("Section_route", __name__)


@Section_routes.route("/section/index")
def section_index():
    return render_template("section_index.html")


@Section_routes.route("/section/get/all")  # check token
def section_get_all():
    return Func.fun_section_get_all()


@Section_routes.route("/section/get/id/<int:id_>")  # check token
def section_get_id(id_: int):
    return Func.func_section_get_id(id_)


# @Section_routes.route("/section/get/create_time/<int:time_>/later")  # check token
# def section_get_create_time_later(time_: int):
#     pass
#
#
# @Section_routes.route("/section/get/create_time/<int:time_>/before")  # check token
# def section_get_create_time_before(time_: int):
#     pass


@Section_routes.route("/section/add", methods=["POST"])  # check token
def section_add():
    function = request.form.get("function") or Setting.Section.Function.UnDefined
    type_ = request.form.get("type") or Setting.Section.Type.RawText
    con = request.form.get("con") or abort(StatusCode.STATUS_CODE_BadRequest)

    return Func.func_section_add(function, type_, con)


# @Section_routes.route("/section/add/multi", methods=["POST"])  # check token
# def section_add_multi():
#     function = request.form.get("function") or Setting.Section.Function.UnDefined
#     if function not in Setting.Section.Function.List:
#         function = Setting.Section.Function.UnDefined
#     type_ = request.form.get("type") or Setting.Section.Type.RawText
#     if type_ not in Setting.Section.Type.List:
#         type_ = Setting.Section.Type.RawText
#     cons = request.form.get("con") or abort(StatusCode.STATUS_CODE_BadRequest)
#     b = DataBody()
#     if type(cons) is list:
#         print(len(cons))
#         db_insert_multi(cons, function, type_)
#         b.Message = "new sections add done"
#     elif type(cons) is str:
#         db_insert(cons, function, type_)
#         b.Message = "new section add done"
#     else:
#         abort(StatusCode.STATUS_CODE_BadRequest)
#     b.Body = []
#     b.StatusCode = 200
#     return b.to_object()


@Section_routes.route("/section/modify/id/<int:id_>", methods=["POST"])  # check token
def section_modify(id_):
    function = request.form.get("function") or None
    type_ = request.form.get("type") or None
    con = request.form.get("con") or None
    return Func.func_section_modify(id_, function, type_, con)


@Section_routes.route("/section/delete/id/<int:id_>", methods=["DELETE"])  # check token
def section_delete_id(id_):
    return Func.func_section_delete_id(id_)

# @Section_routes.route("/section/delete/ids", methods=["DELETE"])  # check token
# def section_delete_ids():
#     pass

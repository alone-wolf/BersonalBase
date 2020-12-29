from flask import Blueprint, render_template, request

from PersonalBase.BaseCApp.apps.Section.func import func_section_delete_id, func_section_modify, func_section_add, \
    func_section_get_id, fun_section_get_all
from PersonalBase.BaseCApp.apps.Section.sectionConfig import SectionConfig
from PersonalBase.BaseCApp import StatusCode
from PersonalBase.Utils.requestUtils import get_standard_request_value


def init_section_blueprint():
    Section_routes = Blueprint("Section_route", __name__)

    @Section_routes.route("/section/index")
    def section_index():
        return render_template("section_index.html")

    @Section_routes.route("/section/get/all")  # check token
    def section_get_all():
        return fun_section_get_all()

    @Section_routes.route("/section/get/id/<int:id_>")  # check token
    def section_get_id(id_: int):
        return func_section_get_id(id_)

    @Section_routes.route("/section/add", methods=["POST"])  # check token
    def section_add():
        form = request.form
        function = get_standard_request_value(form, SectionConfig.Function, "function")
        type_ = get_standard_request_value(form, SectionConfig.Type, "type")
        con = get_standard_request_value(form, SectionConfig.Function, "function", None, StatusCode.Code.STATUS_CODE_BadRequest)
        return func_section_add(function, type_, con)

    @Section_routes.route("/section/modify/id/<int:id_>", methods=["POST"])  # check token
    def section_modify(id_):
        function = request.form.get("function") or None
        type_ = request.form.get("type") or None
        con = request.form.get("con") or None
        return func_section_modify(id_, function, type_, con)

    @Section_routes.route("/section/delete/id/<int:id_>", methods=["DELETE"])  # check token
    def section_delete_id(id_):
        return func_section_delete_id(id_)

    return Section_routes

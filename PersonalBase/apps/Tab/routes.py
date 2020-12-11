import json

from flask import Blueprint, request
from flask_socketio import emit

from PersonalBase.apps.Tab.config import Config
from PersonalBase.apps.Section.route_func import Func
from PersonalBase.apps.Section.utils import DataBody
from PersonalBase.config.error import StatusCode

Tab_routes = Blueprint("Tab_routes", __name__)


@Tab_routes.route("/tab/index")
def tab_index():
    return "404"


@Tab_routes.route("/tab/add", methods=["GET", "POST"])
def tab_add():
    body = DataBody()
    url = request.form.get("url") or request.args.get("url") or None
    title = request.form.get("title") or request.args.get("title") or None
    if not url or not title:
        body.StatusCode = StatusCode.STATUS_CODE_BadRequest
        body.Body = []
        body.Message = "bad request, lack title or url"
        return body.to_object(), 200
    con_body = {
        "title": title,
        "url": url
    }
    emit(Config.WebSocket.ENTRANCE_TAB, body, namespace=Config.WebSocket.NAMESPACE)
    Func.func_section_add(Config.Function, Config.Type, json.dumps(con_body))
    return "new tab add done"


@Tab_routes.route("/tab/get/all", methods=['GET'])
def tab_get_all():
    return Func.func_section_get_function_with_json_con(Config.Function)


@Tab_routes.route("/tab/get/all/thin", methods=['GET'])
def tab_get_all_thin():
    return Func.func_section_get_function_with_json_con_thin(Config.Function)


@Tab_routes.route("/tab/delete/id/<int:id>", methods=['DELETE'])
def tab_delete_id(id_):
    Func.func_section_delete_id(id_, function=Config.Function, type_=Config.Type)


@Tab_routes.route("/tab/delete/all", methods=['DELETE'])
def tab_delete_all():
    body = DataBody()
    body.Body = []
    if Func.func_section_delete_all_function(Config.Function) is -1:
        body.StatusCode = StatusCode.STATUS_CODE_BadRequest
        body.Message = "error delete tab, due to bad function"
        return body.to_object()
    else:
        body.StatusCode = StatusCode.StatusCode_Ok
        body.Message = "delete all tab done"
        return body.to_object()
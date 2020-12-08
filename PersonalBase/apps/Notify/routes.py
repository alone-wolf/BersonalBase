import json

from flask import Blueprint, request, render_template
from flask_socketio import emit

from PersonalBase.apps.Notify.config import Config
from PersonalBase.apps.Section.models import db_insert, db_delete_ids, db_select_function
from PersonalBase.apps.Section.route_func import Func
from PersonalBase.apps.Section.utils import DataBody, get_unix_time_stamp
from PersonalBase.config.error import StatusCode

Notify_routes = Blueprint("Notify_routes", __name__)


@Notify_routes.route("/notify/index", methods=['GET'])
def notify_index():
    return render_template("notify_panel.html")


@Notify_routes.route("/notify", methods=['GET', 'POST'])
def notify_add():
    b = DataBody()
    b.Body = []
    notify = request.form.get("notify") or request.args.get("notify") or None
    if not notify:
        b.StatusCode = StatusCode.STATUS_CODE_BadRequest
        b.Message = "bad notify"
        return b.to_object(), 200
    title = request.form.get("title") or request.args.get("title") or "default title"
    device = request.form.get("device") or request.args.get("device") or "default device"

    body = {
        "notify": notify,
        "title": title,
        "device": device
    }
    body_with_time = {
        "notify": notify,
        "title": title,
        "device": device,
        "time": str(get_unix_time_stamp())
    }

    send_type = request.args.get('sendType') or Config.WebSocket.SEND_TYPE_ALL
    if (send_type != Config.WebSocket.SEND_TYPE_ALL) and (send_type != Config.WebSocket.SEND_TYPE_MONITOR_ONLY):
        send_type = Config.WebSocket.SEND_TYPE_ALL

    if send_type == Config.WebSocket.SEND_TYPE_ALL:
        emit(Config.WebSocket.ENTRANCE_NOTIFY, body_with_time, broadcast=True, namespace=Config.WebSocket.NAMESPACE)
        emit(Config.WebSocket.ENTRANCE_NOTIFY_MONITOR_ONLY, body_with_time, broadcast=True,
             namespace=Config.WebSocket.NAMESPACE)
    elif send_type == Config.WebSocket.SEND_TYPE_MONITOR_ONLY:
        emit(Config.WebSocket.ENTRANCE_NOTIFY_MONITOR_ONLY, body_with_time, broadcast=True,
             namespace=Config.WebSocket.NAMESPACE)
    b.StatusCode = 200
    b.Message = db_insert(json.dumps(body), Config.Function, Config.Type)
    return b.to_object(), 200


@Notify_routes.route("/notify/get/all", methods=['GET'])
def notify_get_all():
    return Func.func_section_get_function_with_json_con(Config.Function)


@Notify_routes.route("/notify/get/all/thin", methods=['GET'])
def notify_get_all_thin():
    return Func.func_section_get_function_with_json_con_thin(Config.Function)


@Notify_routes.route("/notify/delete/all", methods=["DELETE"])
def notify_delete_all():
    b = DataBody()
    b.Body = []
    db_delete_ids([i.id for i in db_select_function(Config.Function)])
    b.StatusCode = 200
    b.Message = "delete all notify done"
    return b.to_object(), 200

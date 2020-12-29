import json
import os

from flask import Blueprint, render_template, request
from flask_socketio import emit

from PersonalBase.BaseCApp.StatusCode import Code
from PersonalBase.BaseCApp.apps.Notify.config import Config
from PersonalBase.BaseCApp.apps.Notify.beam import NotifyCon
from PersonalBase.BaseCApp.apps.Section.func import func_section_add, func_section_get_function_with_json_con, \
    func_section_get_function_with_json_con_thin, func_section_delete_all_function
from PersonalBase.Utils import get_unix_time_stamp, DataBody


def init_notify_blueprint():
    Notify_routes = Blueprint("Notify_routes", __name__,
                              url_prefix="/notify",
                              template_folder="{}/PersonalBase/BaseCApp/apps/Notify/templates".format(os.getcwd()))

    @Notify_routes.route("/index", methods=['GET'])
    def notify_index():
        return render_template("notify_panel.html")

    @Notify_routes.route("/", methods=['GET', 'POST'])
    def notify_add():
        b = DataBody()
        b.Body = []
        notify = get_value_from_request("notify", None)
        if not notify:
            b.StatusCode = Code.STATUS_CODE_BadRequest
            b.Message = "bad notify"
            return b.to_object(), 200

        body_with_time = NotifyCon(
            notify,
            get_value_from_request("title", "default title"),
            get_value_from_request("device", "default device"),
            str(get_unix_time_stamp())).to_object()

        emit_notify_message(get_send_type(), body_with_time)

        return func_section_add(Config.Function, Config.Type, json.dumps(body_with_time))

    @Notify_routes.route("/get/all", methods=['GET'])
    def notify_get_all():
        return func_section_get_function_with_json_con(Config.Function)

    @Notify_routes.route("/get/all/thin", methods=['GET'])
    def notify_get_all_thin():
        return func_section_get_function_with_json_con_thin(Config.Function)

    @Notify_routes.route("/delete/all", methods=["DELETE"])
    def notify_delete_all():
        b = DataBody()
        b.Body = []
        func_section_delete_all_function(Config.Function)
        b.StatusCode = 200
        b.Message = "delete all notify done"
        return b.to_object(), 200

    return Notify_routes


def get_value_from_request(key, default_value):
    return request.form.get(key) or request.args.get(key) or default_value


def get_value_from_args(key, default_value):
    return request.args.get(key) or default_value


def get_value_from_form(key, default_value):
    return request.form.get(key) or default_value


def get_send_type():
    tmp = get_value_from_args('sendType', "all")
    if tmp not in ["all", "monitor"]:
        tmp = "all"
    return tmp


def emit_notify_message(send_type, body_with_time):
    if send_type == "all":
        emit(Config.WebSocket.ENTRANCE.NotifyAll,
             body_with_time, broadcast=True,
             namespace=Config.WebSocket.NAMESPACE)
        emit(Config.WebSocket.ENTRANCE.NotifyMonitorOnly,
             body_with_time, broadcast=True,
             namespace=Config.WebSocket.NAMESPACE)
    elif send_type == "monitor":
        emit(Config.WebSocket.ENTRANCE.NotifyMonitorOnly,
             body_with_time, broadcast=True,
             namespace=Config.WebSocket.NAMESPACE)

import json

from flask import Blueprint, request

from PersonalBase.apps.Section.models import db_insert, db_delete_ids, db_select_function
from PersonalBase.apps.Section.route_func import Func
from PersonalBase.apps.Section.utils import DataBody
from PersonalBase.config import Setting
from PersonalBase.config.errorpage import StatusCode

Notify_routes = Blueprint("Notify_routes", __name__)


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
    b.StatusCode = 200
    b.Message = db_insert(json.dumps(
        {
            "notify": notify,
            "title": title,
            "device": device
        }), Setting.Section.Function.Notify, Setting.Section.Type.Json)
    return b.to_object(), 200


@Notify_routes.route("/notify/get/all", methods=['GET'])
def notify_get_all():
    return Func.func_section_get_function_with_json_con(Setting.Section.Function.Notify)


@Notify_routes.route("/notify/delete/all", methods=["DELETE"])
def notify_delete_all():
    b = DataBody()
    b.Body = []
    # ss = db_select_function(Setting.Section.Function.Notify)
    # l = [i.id_ for i in ss]
    db_delete_ids([i.id for i in db_select_function(Setting.Section.Function.Notify)])
    b.StatusCode = 200
    b.Message = "delete all notify done"
    return b.to_object(), 200

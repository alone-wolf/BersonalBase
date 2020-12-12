from flask import Blueprint, render_template, request, abort, jsonify
from PersonalBase.apps.Door.models import db_insert
from PersonalBase.apps.Door.models import db_select_all
from PersonalBase.common.SQLAlchemy import db
from PersonalBase.common.secure import check_access_token
from PersonalBase.config.setting import Setting

Door_routes = Blueprint('Door_routes', __name__)


@Door_routes.route('/door/index')
def index():
    return render_template("door.html")


@Door_routes.route('/door')
def door():
    if Setting.DoorIsOpen:
        return "Opened"
    else:
        return "Closed"


@Door_routes.route('/door/admin')
def admin():
    return render_template("door_admin.html")


@Door_routes.route('/door/admin/logs')
def admin_logs_():
    door_log_list = []
    for i in db_select_all():
        item = {
            'id': i.id,
            'time': i.time,
            'is_open': i.is_open,
            'user': i.user
        }
        door_log_list.append(item)
    return jsonify(door_log_list)


@Door_routes.route('/door/admin/door', methods=['POST'])
@check_access_token
def admin_door():
    status = request.form.get("status") or abort(400)
    user = request.form.get("user", "blank")
    if status == "Open" and not Setting.DoorIsOpen:
        Setting.DoorIsOpen = True
        db_insert(True, user)
    elif status == "Close" and Setting.DoorIsOpen:
        Setting.DoorIsOpen = False
        db_insert(False, user)

    return "door is " + status


@Door_routes.route('/door/admin/db/init')
@check_access_token
def admin_db_init_():
    db.create_all()
    return "create done"


@Door_routes.route('/door/admin/db/drop')
@check_access_token
def admin_db_init():
    db.drop_all()
    return "drop done"

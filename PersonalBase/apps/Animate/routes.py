import json

from flask import Blueprint, request, abort, render_template

from PersonalBase.apps.Animate.utils import AnimateNode
from PersonalBase.apps.Section.models import db_update_id, db_select_id, db_delete_id
from PersonalBase.apps.Section.route_func import Func
from PersonalBase.apps.Section.utils import DataBody
from PersonalBase.config import Setting
from PersonalBase.config.error import StatusCode

Animate_routes = Blueprint("Animate_routes", __name__)


@Animate_routes.route("/animate/index")
def animate_index():
    return render_template("animate_index.html")


@Animate_routes.route("/animate/get/all")
def animate_get_all():
    return Func.func_section_get_function_with_json_con(Setting.Section.Function.AnimeEpisode)


@Animate_routes.route("/animate/add", methods=["POST"])
def animate_add():
    title = request.form.get("title") or abort(StatusCode.STATUS_CODE_BadRequest)
    current_episode = int(request.form.get("currentEpisode")) or 0
    base_url = request.form.get("baseUrl") or abort(StatusCode.STATUS_CODE_BadRequest)
    site_title = request.form.get("siteTitle") or abort(StatusCode.STATUS_CODE_BadRequest)

    return Func.func_section_add(
        function=Setting.Section.Function.AnimeEpisode,
        type_=Setting.Section.Type.Json,
        con=json.dumps(AnimateNode(title, current_episode, base_url, site_title).to_object())
    )


@Animate_routes.route("/animate/next/id/<int:id_>")
def animate_next_id(id_):
    b = DataBody()
    b.Body = []
    tmp = db_select_id(id_)
    if not tmp:
        abort(404)
    if tmp.function != Setting.Section.Function.AnimeEpisode:
        b.StatusCode = StatusCode.STATUS_CODE_BadRequest
        b.Message = "bad function " + tmp.function
        return b.to_object(), 200
    if tmp.type_ != Setting.Section.Type.Json:
        b.StatusCode = StatusCode.STATUS_CODE_BadRequest
        b.Message = "bad type " + tmp.type_
        return b.to_object(), 200
    con_object = json.loads(tmp.con)
    con_object["currentEpisode"] = int(con_object["currentEpisode"]) + 1
    db_update_id(id_, json.dumps(con_object), None, None)
    b.StatusCode = 200
    b.Message = "animate item update done"
    return b.to_object(), 200


@Animate_routes.route("/animate/delete/id/<int:id_>", methods=['DELETE'])
def animate_delete_id(id_):
    db_delete_id(int(id_))
    b = DataBody()
    b.StatusCode = 200
    b.Message = "animate delete done id=" + str(id_)
    b.Body = []
    return b.to_object()

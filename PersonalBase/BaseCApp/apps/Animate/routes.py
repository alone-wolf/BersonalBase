import json
import os

from flask import Blueprint, request, abort, render_template

from PersonalBase.BaseCApp.StatusCode import Code
from PersonalBase.BaseCApp.apps.Animate.beam import AnimateNode
from PersonalBase.BaseCApp.apps.Animate.config import Config
from PersonalBase.BaseCApp.apps.Section.func import func_section_get_function_with_json_con, func_section_add, \
    func_delete_id, func_update_id, func_select_id
from PersonalBase.Utils import DataBody


def init_animate_blueprint():
    Animate_routes = Blueprint("Animate_routes", __name__,
                               url_prefix="/animate",
                               template_folder="{}/PersonalBase/BaseCApp/apps/Animate/templates".format(os.getcwd()))

    @Animate_routes.route("/index", methods=['GET'])
    def index():
        return render_template("animate_index.html")

    @Animate_routes.route("/get/all", methods=["GET"])
    def get_all():
        return func_section_get_function_with_json_con(Config.Function)

    @Animate_routes.route("/add", methods=["POST"])
    def add():
        title = request.form.get("title") or abort(Code.STATUS_CODE_BadRequest)
        current_episode = int(request.form.get("currentEpisode")) or 0
        base_url = request.form.get("baseUrl") or abort(Code.STATUS_CODE_BadRequest)
        site_title = request.form.get("siteTitle") or abort(Code.STATUS_CODE_BadRequest)
        return func_section_add(
            function=Config.Function,
            type_=Config.Type,
            con=json.dumps(AnimateNode(title, current_episode, base_url, site_title).to_object())
        )

    @Animate_routes.route("/next/id/<int:id_>")
    def animate_next_id(id_):
        b = DataBody()
        b.Body = []
        tmp = func_select_id(id_)
        if not tmp:
            abort(404)
        if tmp.function != Config.Function:
            b.StatusCode = Code.STATUS_CODE_BadRequest
            b.Message = "bad function " + tmp.function
            return b.to_object(), 200
        if tmp.type_ != Config.Type:
            b.StatusCode = Code.STATUS_CODE_BadRequest
            b.Message = "bad type " + tmp.type_
            return b.to_object(), 200
        con_object = json.loads(tmp.con)
        con_object["currentEpisode"] = int(con_object["currentEpisode"]) + 1
        func_update_id(id_, json.dumps(con_object), None, None)
        b.StatusCode = 200
        b.Message = "animate item update done"
        return b.to_object(), 200

    @Animate_routes.route("/delete/id/<int:id_>", methods=['DELETE'])
    def animate_delete_id(id_):
        func_delete_id(int(id_))
        b = DataBody()
        b.StatusCode = 200
        b.Message = "animate delete done id=" + str(id_)
        b.Body = []
        return b.to_object()

    return Animate_routes

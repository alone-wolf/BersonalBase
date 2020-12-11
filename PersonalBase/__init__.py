from flask import Flask, jsonify, request,abort
from PersonalBase.apps import init_apps
from PersonalBase.common.Admin import init_admin
from PersonalBase.common.WebSocket import init_websocket
from PersonalBase.config import init_config
from PersonalBase.common.ext import init_ext


def create_server():
    server = Flask(__name__)

    init_apps(server)
    server = init_config(server)
    init_ext(server)  # sql ctrl
    # init_admin(server)

    @server.before_request
    def check_access_token():
        # print(request.path)
        if request.headers.get("access_token") == "asdfghjkl":
            return
        elif str(request.path).endswith("/index"):
            return
        elif str(request.path).startswith("/socket.io"):
            return
        elif str(request.path).startswith("/animate"):
            return
        else:
            abort(401)

    @server.after_request
    def add_global_headers(response):
        response.headers["Author-Tag"] = "alone-wolf"
        return response

    @server.route("/apis")
    def apis():
        url_map = str(server.url_map)[5:-2]
        url_map = url_map.split('<Rule')[1:]
        url_map_tmp = []
        for i in range(len(url_map) - 1):
            a = url_map[i][1:-3]
            url_map_tmp.append(a)
        url_map_tmp.append(url_map[-1][1:])

        url_map_tmp_1_route = []
        url_map_tmp_2_method = []
        url_map_tmp_3_endpoint = []
        for i in url_map_tmp:
            tmp = i.split('->')
            tmp_tmp = tmp[0].split('(')
            url_map_tmp_1_route.append(tmp_tmp[0][1:-2])
            url_map_tmp_2_method.append(tmp_tmp[1][:-2])
            url_map_tmp_3_endpoint.append(tmp[1][1:-1])
        route = []
        for i in range(len(url_map_tmp_1_route)):
            route_node = {
                'route': url_map_tmp_1_route[i],
                'methods': url_map_tmp_2_method[i].split(', '),
                'endpoint': url_map_tmp_3_endpoint[i]}
            route.append(route_node)
        # route.sort(key=takeRoute)
        return jsonify(route)

    return init_websocket(server), server

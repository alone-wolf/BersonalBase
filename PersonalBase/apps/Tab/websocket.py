from flask_socketio import emit

# socketio定义 以客户端为标定物 on的叫en_xxx entity  emit的叫ev_xxx event
#                相应的服务端 on ev_xxx emit en_xxx
debug = True


def init_websocket_tab_liquid(socket_):
    # 第一期工程
    @socket_.on('ev_tab_liquid_send', namespace="/root_ns")
    def ev_tab_liquid_send(message):
        emit('en_tab_liquid', {'data': message.get("data")}, broadcast=True, include_self=debug)

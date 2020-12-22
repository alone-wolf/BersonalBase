from flask import session
from flask_socketio import emit

from PersonalBase.config import Setting


# socketio定义 以客户端为标定物 on的叫en_xxx entity  emit的叫ev_xxx event
#                相应的服务端 on ev_xxx emit en_xxx
def init_websocket_tab_liquid(socket_):
    # 第一期工程
    @socket_.on('ev_tab_liquid_send', namespace=Setting.WebSocket.ROOT_NAMESPACE)
    def tab_work(message):
        session['receive_count'] = session.get('receive_count', 0) + 1
        emit('en_tab_liquid',
             {'data': message['data'], 'count': session['receive_count']}, broadcast=True)

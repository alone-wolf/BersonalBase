from flask import session
from flask_socketio import SocketIO, emit

from PersonalBase.apps.Notify.config import Config


def init_websocket(server):
    async_mode = None
    socket_ = SocketIO(server, async_mode=async_mode)

    @socket_.on('my_ping', namespace=Config.WebSocket.NAMESPACE)
    def test_message(message):
        session['receive_count'] = session.get('receive_count', 0) + 1
        emit('my_pong',
             {'data': message['data'], 'count': session['receive_count']})

    return socket_

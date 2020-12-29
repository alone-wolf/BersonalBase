from flask import session
from flask_socketio import SocketIO, emit

from PersonalBase.Configure import Setting


def init_socket_io_main(server_app):
    socket_io = SocketIO(server_app, async_mode=None, cors_allowed_origins="*")

    @socket_io.on('my_ping', namespace=Setting.SocketIO.ROOT_NAMESPACE)
    def test_message(message):
        session['receive_count'] = session.get('receive_count', 0) + 1
        emit('my_pong',
             {'data': message['data'], 'count': session['receive_count']})

    return socket_io

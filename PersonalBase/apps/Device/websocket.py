from flask import session
from flask_socketio import emit

from PersonalBase.config import Setting


def init_websocket_device(socket_):
    @socket_.on('device_report', namespace=Setting.WebSocket.ROOT_NAMESPACE)
    def test_message(message):
        session['receive_count'] = session.get('receive_count', 0) + 1
        emit('device_info_broadcast',
             {'data': message['data'], 'count': session['receive_count']}, broadcast=True)

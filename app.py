from website import create_app
from flask_socketio import SocketIO, emit

app = create_app()
socketio = SocketIO(app)

@socketio.on('socketEvent')
def socketEvent(data):
    emit('socketEvent', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app=app, host='127.0.0.1', port=5000, debug=True)

    # gunicorn --worker-class eventlet -w 1 app:app -b 127.0.0.1:5000
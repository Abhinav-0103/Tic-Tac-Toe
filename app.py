from flask import Flask, render_template
from flask_socketio import SocketIO
from createapp import create_app

socketio = SocketIO()

if __name__ == '__main__':
    app = create_app()
    socketio.init_app(app)
    socketio.run(app)
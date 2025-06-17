from flask import Flask, render_template
from flask_socketio import SocketIO
from createapp import create_app

socketio = SocketIO()

if __name__ == '__main__':
    app = create_app()
    socketio.init_app(app)

    @socketio.on("connect")
    def handle_connect() :
        print("Client Connected")

    @socketio.on("join")
    def handle_join() :
        print("Player has joined")

    socketio.run(app, debug=True)
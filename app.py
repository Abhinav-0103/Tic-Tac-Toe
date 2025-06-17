from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, leave_room
from createapp import create_app
from collections import defaultdict

rooms = defaultdict(list)
socketio = SocketIO()

if __name__ == '__main__':
    app = create_app()
    socketio.init_app(app)

    @socketio.on("connect")
    def handle_connect() :
        print("----------------------------")
        print("Client Connected")
        print("----------------------------")

    @socketio.on("join")
    def handle_join(data) :
        print(f"{data['name']} has joined: {data['id']}")
        join_room(data["id"])

    @socketio.on("player_move")
    def handle_move(data, cell_id) :
        print(f"{data['name']} has made a move on cell {cell_id}")

    socketio.run(app, debug=True)
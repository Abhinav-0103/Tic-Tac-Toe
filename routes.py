from flask import Flask, render_template, redirect
import uuid

def create_routes(app) :
    @app.route("/")
    def index() :
        return render_template("login.html")
    
    @app.route("/gamecode")
    def game_code() :
        return render_template("join.html")
    
    @app.route("/room/<id>")
    def game_room(id) :
        return render_template("game.html")
    
    @app.route("/create_room", methods=["POST"])
    def create_room() :
        roomid = str(uuid.uuid4())
        return redirect(f"/room/{roomid}")
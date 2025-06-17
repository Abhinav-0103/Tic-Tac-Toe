from flask import Flask, render_template, redirect, request, url_for
import uuid
from collections import defaultdict

def create_routes(app) :
    @app.route("/")
    def index() :
        return render_template("login.html")
    
    @app.route("/gamecode")
    def game_code() :
        return render_template("join.html")
    
    @app.route("/room/<id>")
    def game_room(id) :
        name = request.args.get("name")
        return render_template("game.html", id=id, name=name)
    
    @app.route("/create_room", methods=["POST"])
    def create_room() :
        name = request.form.get("username")
        roomid = str(uuid.uuid4())
        return redirect(url_for("game_room", id=roomid, name=name))
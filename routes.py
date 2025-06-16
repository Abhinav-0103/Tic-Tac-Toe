from flask import Flask, render_template

def create_routes(app) :
    @app.route("/")
    def index() :
        return render_template("join.html")
    
    @app.route("/game")
    def game() :
        return render_template("game.html")
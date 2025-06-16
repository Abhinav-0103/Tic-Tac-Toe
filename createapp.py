from flask import Flask, render_template
from flask_socketio import SocketIO
from routes import create_routes

def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static", static_url_path="/")
    app.config['SECRET_KEY'] = 'secret!'

    create_routes(app)
    
    return app
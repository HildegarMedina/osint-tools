from flask import Flask
from routes.home import home as home_route

app = Flask(__name__)

app.register_blueprint(home_route)
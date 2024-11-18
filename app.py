from flask import Flask
from routes.dashboard import dashboard as dashboard_route
from routes.history import history as history_route
from routes.settings import settings as settings_route

app = Flask(__name__)

app.register_blueprint(dashboard_route)
app.register_blueprint(history_route)
app.register_blueprint(settings_route)

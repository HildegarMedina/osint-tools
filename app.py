from flask import Flask
from routes.dashboard import route as dashboard_route
from routes.history import route as history_route
from routes.settings import route as settings_route
from config.config import SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY
app.config['SESSION_TYPE'] = 'filesystem'

app.register_blueprint(dashboard_route)
app.register_blueprint(history_route)
app.register_blueprint(settings_route)

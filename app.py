from flask import Flask
from routes import (
    dashboard,
    history,
    settings,
    ip_geolocation,
    phone_geolocation,
    domain_gathering,
    google_dorks
)
from config.config import SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY
app.config['SESSION_TYPE'] = 'filesystem'

app.register_blueprint(dashboard.route)
app.register_blueprint(history.route)
app.register_blueprint(settings.route)
app.register_blueprint(ip_geolocation.route)
app.register_blueprint(phone_geolocation.route)
app.register_blueprint(domain_gathering.route)
app.register_blueprint(google_dorks.route)

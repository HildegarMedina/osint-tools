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
from config.config import SECRET_KEY, AVAILABLE_TOOLS
from database import db
from domain.models import *

app = Flask(__name__)
app.secret_key = SECRET_KEY
app.config['SESSION_TYPE'] = 'filesystem'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///osint-tool.db"

def tool_filter(tool):
    
    tools = {tool["code"]: tool["name"] for tool in AVAILABLE_TOOLS}
    return tools.get(tool, tool)

app.jinja_env.filters['tool'] = tool_filter

app.register_blueprint(dashboard.route)
app.register_blueprint(history.route)
app.register_blueprint(settings.route)
app.register_blueprint(ip_geolocation.route)
app.register_blueprint(phone_geolocation.route)
app.register_blueprint(domain_gathering.route)
app.register_blueprint(google_dorks.route)

db.init_app(app)

with app.app_context():
    db.create_all()

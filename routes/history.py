from flask import Blueprint, render_template
from services.history import History
from database import db

route = Blueprint('history', __name__, url_prefix='/history')

history_svc = History(db)

@route.route('/')
def index():
    history = history_svc.get_list()
    return render_template('pages/history.html', history=history)

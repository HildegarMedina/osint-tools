from flask import Blueprint, render_template
from services.history import History
from database import db

router = Blueprint('history', __name__, url_prefix='/history')

history_svc = History(db)

@router.route('/')
def index():
    history = history_svc.get_list()
    return render_template('pages/history.html', history=history)

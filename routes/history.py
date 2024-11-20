from flask import Blueprint, render_template

route = Blueprint('history', __name__, url_prefix='/history')

@route.route('/')
def index():
    return render_template('pages/history.html')

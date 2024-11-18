from flask import Blueprint, render_template

history = Blueprint('history', __name__, url_prefix='/history')

@history.route('/')
def index():
    return render_template('pages/history.html')

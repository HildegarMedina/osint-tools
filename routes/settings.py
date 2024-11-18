from flask import Blueprint, render_template

settings = Blueprint('settings', __name__, url_prefix='/settings')

@settings.route('/')
def index():
    return render_template('pages/settings.html')

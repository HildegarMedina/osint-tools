from flask import Blueprint, render_template
from config.config import AVAILABLE_TOOLS

router = Blueprint('dashboard', __name__)

@router.route('/')
def index():
    return render_template('pages/dashboard.html', tools=AVAILABLE_TOOLS)

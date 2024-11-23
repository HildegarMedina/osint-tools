from flask import Blueprint, render_template, request, flash, redirect, url_for
from services.settings import Settings
from dotenv import load_dotenv

load_dotenv()

router = Blueprint('settings', __name__, url_prefix='/settings')
settings_svc = Settings()

@router.route('/')
def index():
    settings = settings_svc.get_all()
    return render_template('pages/settings.html', settings=settings)

@router.route('/', methods=['POST'])
def update_settings():
    ipinfo_token = request.form.get('ipinfo_token')
    openai_api_key = request.form.get('openai_api_key')
    if settings_svc.update({
        'ipinfo_token': ipinfo_token,
        'openai_api_key': openai_api_key
    }):
        flash('Settings updated successfully!', 'success')
    return redirect(url_for('settings.index'))

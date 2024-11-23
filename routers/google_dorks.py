from flask import Blueprint, render_template, request, redirect, flash, jsonify
from dotenv import get_key
from modules.chatgpt import ChatGPT
from services.google_dork import GoogleDork
from services.history import History
from database import db

router = Blueprint('google_dorks', __name__)

chatgpt = ChatGPT()
google_dork_svc = GoogleDork(chatgpt)
history_svc = History(db)

@router.route('/google-dorks', methods=['GET'])
def index():
    if not get_key('.env', 'OPENAI_API_KEY'):
        flash('OpenAI API Key is not set. Please set it in the settings page.', 'error')
        return redirect('/settings')
    return render_template('pages/google_dorks/index.html')

@router.route('/google-dorks/generate', methods=['POST'])
def generate():
    description = request.json.get('description')
    if not description:
        return jsonify({'error': 'Description is required'}), 400
    dork = google_dork_svc.generate(description)
    history_svc.save({"tool": "google-dorks", "input": description})
    return jsonify({
        "dork": dork.replace("Google Dork: ", "")
    })

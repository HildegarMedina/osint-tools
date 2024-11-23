from flask import Blueprint, render_template, request, redirect, flash, jsonify
from modules.chatgpt import ChatGPT
from services.google_dork import GoogleDork
from dotenv import get_key

router = Blueprint('google_dorks', __name__)

chatgpt = ChatGPT()
google_dork = GoogleDork(chatgpt)

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
    dork = google_dork.generate(description)
    return jsonify({
        "dork": dork.replace("Google Dork: ", "")
    })

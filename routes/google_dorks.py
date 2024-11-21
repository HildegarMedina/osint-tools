from flask import Blueprint, render_template, request, redirect, flash

route = Blueprint('google_dorks', __name__)

@route.route('/google-dorks', methods=['GET'])
def index():
    return render_template('pages/ip_geolocation/index.html')

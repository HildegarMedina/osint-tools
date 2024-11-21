from flask import Blueprint, render_template, request, redirect, flash

route = Blueprint('domain_gathering', __name__)

@route.route('/domain-gathering', methods=['GET'])
def index():
    return render_template('pages/ip_geolocation/index.html')

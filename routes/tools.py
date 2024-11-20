from flask import Blueprint, render_template

route = Blueprint('tools', __name__)

@route.route('/ip-geolocation')
def ip_geolocation():
    return render_template('pages/tools/ip_geolocation.html')

@route.route('/number-geolocation')
def number_geolocation():
    return render_template('pages/tools/number_geolocation.html')

@route.route('/domain-gathering')
def domain_gathering():
    return render_template('pages/tools/domain_gathering.html')

@route.route('/google-dorks')
def google_dorks():
    return render_template('pages/tools/google_dorks.html')
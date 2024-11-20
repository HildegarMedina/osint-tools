from flask import Blueprint, render_template, request
from services.ip_geolocation import IpGeolocation

route = Blueprint('tools', __name__)
ip_geolocation_svc = IpGeolocation()

@route.route('/ip-geolocation', methods=['GET'])
def ip_geolocation():
    return render_template('pages/tools/ip_geolocation/index.html')

@route.route('/ip-geolocation', methods=['POST'])
def lookup_ip_geolocation():
    ip_address = request.form['ip_address']
    details = ip_geolocation_svc.get_details(ip_address)
    map = ip_geolocation_svc.draw_map(details["latitude"], details["longitude"], details["loc"])
    return render_template('pages/tools/ip_geolocation/details.html', details=details, map=map)

@route.route('/number-geolocation')
def number_geolocation():
    return render_template('pages/tools/number_geolocation.html')

@route.route('/domain-gathering')
def domain_gathering():
    return render_template('pages/tools/domain_gathering.html')

@route.route('/google-dorks')
def google_dorks():
    return render_template('pages/tools/google_dorks.html')
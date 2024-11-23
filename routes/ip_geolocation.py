from flask import Blueprint, render_template, request, redirect, flash
from services.ip_geolocation import IpGeolocation

route = Blueprint('ip_geolocation', __name__)

ip_geolocation_svc = IpGeolocation()

@route.route('/ip-geolocation', methods=['GET'])
def index():
    return render_template('pages/ip_geolocation/index.html')

@route.route('/ip-geolocation', methods=['POST'])
def lookup_ip_geolocation():
    ip_address = request.form['ip_address']
    details = ip_geolocation_svc.get_details(ip_address)
    if details and details.get("latitude") and details.get("longitude"):
        map = ip_geolocation_svc.draw_map(details["latitude"], details["longitude"], details["loc"])
        details = {
            "ip": details.get("ip"),
            "country_flag_url": details.get("country_flag_url"),
            "data": ip_geolocation_svc.map_ip_info(details)
        }
        return render_template('pages/ip_geolocation/details.html', details=details, map=map)
    flash('Invalid IP address', 'error')
    return redirect('/ip-geolocation')

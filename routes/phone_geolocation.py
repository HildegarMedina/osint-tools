from flask import Blueprint, render_template, request, redirect, flash
from database import db
from services.log import Log
from services.phone_geolocation import PhoneGeolocation

route = Blueprint('phone_geolocation', __name__)

log_svc = Log(db)
phone_geolocation = PhoneGeolocation()

@route.route('/phone-geolocation')
def index():
    return render_template('pages/phone_geolocation/index.html')

@route.route('/phone-geolocation', methods=['POST'])
def lookup_phone_geolocation():
    phone_number = request.form['phone_number']
    details = phone_geolocation.get_details(phone_number)
    if details and details["data"].get("Country"):
        log_svc.save({"tool": "phone-geolocation", "input": phone_number})
        return render_template('pages/phone_geolocation/details.html', details=details)
    flash('Invalid phone number', 'error')
    return redirect('/phone-geolocation')

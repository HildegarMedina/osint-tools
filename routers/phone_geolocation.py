from flask import Blueprint, render_template, request, redirect, flash
from database import db
from services.history import History
from services.phone_geolocation import PhoneGeolocation

router = Blueprint('phone_geolocation', __name__)

history_svc = History(db)
phone_geolocation = PhoneGeolocation()

@router.route('/phone-geolocation')
def index():
    return render_template('pages/phone_geolocation/index.html')

@router.route('/phone-geolocation', methods=['POST'])
def lookup_phone_geolocation():
    phone_number = request.form['phone_number']
    details = phone_geolocation.get_details(phone_number)
    if details and details["data"].get("Country"):
        history_svc.save({"tool": "phone-geolocation", "input": phone_number})
        return render_template('pages/phone_geolocation/details.html', details=details)
    flash('Invalid phone number', 'error')
    return redirect('/phone-geolocation')

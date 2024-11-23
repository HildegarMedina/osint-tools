from flask import Blueprint, render_template, request, redirect, flash
from database import db
from services.domain_gathering import DomainGathering
from services.history import History

route = Blueprint('domain_gathering', __name__)

history_svc = History(db)
domain_gathering_svc = DomainGathering()

@route.route('/domain-gathering', methods=['GET'])
def index():
    return render_template('pages/domain_gathering/index.html')

@route.route('/domain-gathering', methods=['POST'])
def domain_gathering():
    domain = request.form.get('domain')
    details = domain_gathering_svc.get_details(domain)
    if details['whois_info']:
        history_svc.save({"tool": "domain-gathering", "input": domain})
        return render_template('pages/domain_gathering/details.html', details=details)
    else:
        flash('Domain not found', 'error')
        return redirect('/domain-gathering')

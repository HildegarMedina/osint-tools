from flask import Blueprint, render_template, request, redirect, flash
from services.domain_gathering import DomainGathering

route = Blueprint('domain_gathering', __name__)
domain_gathering_svc = DomainGathering()

@route.route('/domain-gathering', methods=['GET'])
def index():
    return render_template('pages/domain_gathering/index.html')

@route.route('/domain-gathering', methods=['POST'])
def domain_gathering():
    domain = request.form.get('domain')
    details = domain_gathering_svc.get_details(domain)
    if details['whois_info']:
        return render_template('pages/domain_gathering/details.html', details=details)
    else:
        flash('Domain not found', 'error')
        return redirect('/domain-gathering')

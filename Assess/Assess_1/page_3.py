# Event details

from flask import Blueprint, render_template

details_bp = Blueprint('third', __name__)

@details_bp.route('/details/')
def event_details():
    return render_template('event_details.html')


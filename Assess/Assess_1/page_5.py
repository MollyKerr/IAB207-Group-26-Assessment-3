# Under construction

from flask import Blueprint, render_template

construction_bp = Blueprint('fifth', __name__)

@construction_bp.route('/construction/')
def construction():
    return render_template('under_construction.html')
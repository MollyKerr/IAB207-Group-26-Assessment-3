# event_create_update

from flask import Blueprint, render_template

create_update_bp = Blueprint('second', __name__)

@create_update_bp.route('/create/')
def create_update():
    return render_template('event_create_update.html')
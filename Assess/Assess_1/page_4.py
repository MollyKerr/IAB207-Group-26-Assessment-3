# Booking history

from flask import Blueprint, render_template

history_bp = Blueprint('forth', __name__)

@history_bp.route('/bookings/')
def history():
    return render_template('booking_history.html')
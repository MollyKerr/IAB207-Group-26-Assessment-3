from flask import Flask


def create_app():
    app = Flask(__name__)

    
    # Pages
    from . import page_1 # Index page
    app.register_blueprint(page_1.mainbp)
    from . import page_2 # Create update page
    app.register_blueprint(page_2.create_update_bp)
    from . import page_3 # Event details page
    app.register_blueprint(page_3.details_bp)
    from . import page_4 # Booking history page
    app.register_blueprint(page_4.history_bp)
    from . import page_5 # Page under construction
    app.register_blueprint(page_5.construction_bp)

    return app
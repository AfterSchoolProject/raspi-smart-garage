from flask import Flask

def create_app():
    app = Flask(__name__)

    from . import activate
    app.register_blueprint(activate.bp)

    return app

from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET'] = 'dev_key'

    from .routes import main
    app.register_blueprint(main)

    return app
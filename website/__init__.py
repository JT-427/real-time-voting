from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
from dotenv import load_dotenv
load_dotenv()

db = SQLAlchemy()

def create_app(config_file="config.py"):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10)
    
    db.init_app(app)

    from .client import client
    from .main import main
    app.register_blueprint(client, url_prefix='')
    app.register_blueprint(main, url_prefix='/main')
    
    from .cli import command
    app.register_blueprint(command, cli_group=None)

    return app
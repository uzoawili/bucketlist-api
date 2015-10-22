from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from config import config



# instantiate 'app-facing' flask extensions:
db = SQLAlchemy()

def create_app(config_name):
    """ Creates and configures the flask application.
        Initializes app-facing extensions on the app.
        Registers the blueprints on the app.
    """

    # instantiate the flask application:
    app = Flask(__name__)

    # fetch the current configuration vars:
    current_config = config[config_name]

    # load the flask applications config from current_config
    app.config.from_object(current_config)

    # run any config level initialization:
    current_config.init_app(app)

    # initialize extensions:
    db.init_app(app)

    # reister blueprints:
    from .api_1_0 import api as api_1_0_blueprint
    app.register_blueprint(api_1_0_blueprint, url_prefix='/api/v1.0')

    return app


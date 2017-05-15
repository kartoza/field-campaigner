import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from reporter import reporter
from campaign_manager import campaign_manager
import utilities

osm_app = Flask(__name__, static_folder='./reporter/static')
osm_app.register_blueprint(reporter)
osm_app.register_blueprint(campaign_manager, url_prefix='/campaign_manager')
osm_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

try:
    osm_app.config.from_object(os.environ['APP_SETTINGS'])
except KeyError:
    from app_config import DevelopmentConfig
    osm_app.config.from_object(DevelopmentConfig)

db = SQLAlchemy(osm_app)

# Models
from campaign_manager.models import OsmUser

# Admin setting

admin = Admin(osm_app, name='osm_reporter', template_mode='bootstrap3')

admin.add_view(ModelView(OsmUser, db.session))

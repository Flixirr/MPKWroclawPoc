from flask import Flask
from flask_appbuilder import AppBuilder
from flask_appbuilder.security.mongoengine.manager import SecurityManager
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'mpk-poc',
    'host': '127.0.0.1',
    'port': 27017
}
db = MongoEngine()
appbuilder = AppBuilder(app, security_manager_class=SecurityManager)

from app import models, views
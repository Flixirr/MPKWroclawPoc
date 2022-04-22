from flask import Flask
from flask_appbuilder import AppBuilder
from flask_appbuilder.security.mongoengine.manager import SecurityManager
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'mpk',
    'host': 'mongodb://localhost',
    'port': 5000
}
db = MongoEngine()
appbuilder = AppBuilder(app, security_manager_class=SecurityManager)
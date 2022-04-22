from flask import Blueprint
import models

route_bp = Blueprint('route', __name__)

@route_bp.route('/route/get')
def get_route():
    pass

@route_bp.route('route/post')
def post_route():
    pass

@route_bp.route('route/put')
def put_route():
    pass

@route_bp.route('route/delete')
def delete_route():
    pass

@route_bp.route('route/import-file-data')
def insert_file_data():
    pass
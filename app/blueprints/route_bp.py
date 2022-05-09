import json
from flask import Blueprint, request, jsonify
from flask.views import MethodView
from app.models.city import City
from app.models.route import Route

route_bp = Blueprint('route', __name__)

class CitiesView(MethodView):
    def get(self):
        cities =  City.objects()
        cities_json = cities.to_json()
    
        return jsonify(json.loads(cities_json))

class RoutesView(MethodView):
    def get(self):
        routes = Route.objects()
        routes_json = routes.to_json()

        return jsonify(json.loads(routes_json))

route_bp.add_url_rule('/cities/get/all', view_func=CitiesView.as_view('cities_view'), methods=['GET'])
route_bp.add_url_rule('/routes/get/all', view_func=RoutesView.as_view('routes_view'), methods=['GET'])

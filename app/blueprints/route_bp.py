import json
from flask import Blueprint, request, jsonify, Response
from flask.views import MethodView
from app.models.city import City
from app.models.route import Route
from app.models.trip import Trip
from app.models.stop import Stop
from mongoengine import DoesNotExist

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

class GetTrip(MethodView):
    def post(self):
        request_body = request.get_json()

        if 'trip_id' in request_body:
            try:
                trip_model = Trip.objects.get(trip_id = request_body['trip_id'])
                return jsonify(json.loads(trip_model.to_json()))
            except DoesNotExist:
                return Response({'Given trip does not exist'}, status=400)

class GetStop(MethodView):
    def post(self):
        request_body = request.get_json()

        if 'stop_name' in request_body:
            try:
                stop_model = Stop.objects(name = request_body['stop_name'])[0]
                return jsonify(json.loads(stop_model.to_json()))
            except DoesNotExist:
                return Response({'Given stop does not exist'}, status=400)

route_bp.add_url_rule('/cities/get/all', view_func=CitiesView.as_view('cities_view'), methods=['GET'])
route_bp.add_url_rule('/routes/get/all', view_func=RoutesView.as_view('routes_view'), methods=['GET'])
route_bp.add_url_rule('/trips/get/', view_func=GetTrip.as_view('get_trip'), methods=['POST'])
route_bp.add_url_rule('/stops/get/', view_func=GetStop.as_view('get_stop'), methods=['POST'])

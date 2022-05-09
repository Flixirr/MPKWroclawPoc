from datetime import datetime
import json
from flask import Blueprint, request, jsonify, Response
from flask.views import MethodView

from app.models.stop import Stop
from app.models.stop_times import StopTimes

closest_bp = Blueprint('closest', __name__)

class CalculateDistance(MethodView):
    def get(self):
        request_body = request.get_json()

        age = int(request_body['age'])
        
        if age > 0 and age < 16:
            distance = 1000
        elif age < 26:
            distance = 5000
        elif age < 35:
            distance = 2000
        elif age < 51:
            distance = 1000
        elif age < 66:
            distance = 500
        elif age > 65:
            distance = 100
        else:
            return Response({'Age does not meet requirements: age > 0'}, status=400)

        lat = request_body['lat']
        lon = request_body['lon']

        if 'time' not in request_body:
            departure_time = datetime.now()
        else:
            departure_time = datetime.strptime(request_body['time'], "%H:%M:%S")
        
        if lon > 180 or lon < -180:
            return Response({'Longitude does not meet requirements: <-180, 180>'}, status=400)
        elif lat > 90 or lat < -90:
            return Response({'Latitude does not meet requirements: <-90, 90>'}, status=400)

        near_stops = Stop.objects(lat_lon__near=[lat, lon], lat_lon__max_distance=distance)[:5]

        stops_at_given_time = StopTimes.objects(departure_time__gte=departure_time, stop__in=near_stops).order_by('departure_time')[:5]

        response_json = stops_at_given_time.to_json()

        return jsonify(json.loads(response_json))


closest_bp.add_url_rule('/closest/get', view_func=CalculateDistance.as_view('distance'), methods=['GET'])
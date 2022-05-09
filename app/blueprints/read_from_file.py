from ast import Str
from datetime import datetime
from flask import Blueprint, request, jsonify
from flask.views import MethodView
from csv import reader
import os

from app.models.city import City
from app.models.route import Route
from app.models.stop import Stop
from app.models.stop_times import StopTimes
from app.models.trip import Trip

read_from_file = Blueprint('read_from_file', __name__)

class CitiesReadFile(MethodView):
    def post(self):
        with open(os.path.join(os.getcwd(), "data/cities.csv"), encoding='utf-8') as f:
            file_reader = reader(f)
            next(file_reader)
            for line in file_reader:
                model = City()
                model.city_id = line[0]
                model.name = line[1]

                model.save()
        
        response = {'code': '200'}

        return jsonify(response)

class RoutesReadFile(MethodView):
    def post(self):
        with open(os.path.join(os.getcwd(), "data/routes.csv"), encoding='utf-8') as f:
            file_reader = reader(f)
            next(file_reader)

            for line in file_reader:
                model = Route()
                model.route_id = line[0]
                model.short_name = line[2]
                model.description = line[4]

                model.save()
        
        response = {'code': '200'}

        return jsonify(response)

class StopsReadFile(MethodView):
    def post(self):
        with open(os.path.join(os.getcwd(), "data/stops.csv"), encoding='utf-8') as f:
            file_reader = reader(f)
            next(file_reader)

            for line in file_reader:
                model = Stop()
                model.stop_id = line[0]
                model.code = line[1]
                model.name = line[2]
                model.lat_lon = [float(line[3]), float(line[4])]

                model.save()
        
        response = {'code': '200'}

        return jsonify(response)

class StopTimesReadFile(MethodView):
    def post(self):
        with open(os.path.join(os.getcwd(), "data/stop_times.csv"), encoding='utf-8') as f:
            file_reader = reader(f)
            next(file_reader)

            for line in file_reader:
                model = StopTimes()
                try:
                    model.trip = Trip.objects.get(trip_id = line[0])
                except:
                    continue
                try:
                    model.stop = Stop.objects.get(stop_id = line[3])
                except:
                    continue
                hour = int(line[2].split(':')[0])
                if hour >= 24:
                    hour -= 24
                time = line[2].split(':')

                time[0] = str(hour)

                time = datetime.strptime(':'.join(time), "%H:%M:%S")
                model.departure_time = time

                model.save()
                
            
        response = {'code': '200'}

        return jsonify(response)

class TripsReadFile(MethodView):
    def post(self):

        with open(os.path.join(os.getcwd(), "data/trips.csv"), encoding='utf-8') as f:
            file_reader = reader(f)
            next(file_reader)

            for line in file_reader:
                model = Trip()

                model.trip_id = line[2]
                model.trip_headsign = line[3]
                model.direction_id = line[4]
                model.service_id = line[1]
                try:
                    model.route = Route.objects.get(route_id = line[0])
                except:
                    continue

                model.save()

        response = {'code': '200'}

        return jsonify(response)

read_from_file.add_url_rule('/file/insert/cities', view_func=CitiesReadFile.as_view('cities'), methods=['POST'])
read_from_file.add_url_rule('/file/insert/routes', view_func=RoutesReadFile.as_view('routes'), methods=['POST'])
read_from_file.add_url_rule('/file/insert/stop-times', view_func=StopTimesReadFile.as_view('stop_times'), methods=['POST'])
read_from_file.add_url_rule('/file/insert/stops', view_func=StopsReadFile.as_view('stops'), methods=['POST'])
read_from_file.add_url_rule('/file/insert/trips', view_func=TripsReadFile.as_view('trips'), methods=['POST'])
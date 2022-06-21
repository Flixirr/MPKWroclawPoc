import json
from flask import Blueprint, request, jsonify, Response
from flask.views import MethodView
from app.models.user import User
from app.models.trip import Trip
from mongoengine import DoesNotExist
import uuid

user_bp = Blueprint('user', __name__)

class RegisterUser(MethodView):
    def post(self):
        request_body = request.get_json()
        new_user = User()
        if not 'username' in request_body and not 'password' in request_body:
            return Response({'Missing username or password'}, status=400)
        try:
            if User.objects.get(username = request_body['username']):
                return Response({'Username already exists'}, status=400)
        except DoesNotExist:
            new_user.user_id = uuid.uuid4().hex
            new_user.username = request_body['username']
            new_user.password = request_body['password']

            new_user.save()

        return jsonify(json.loads(new_user.to_json()))

class TripsFavourite(MethodView):
    def post(self):
        request_body = request.get_json()

        if 'username' in request_body and 'trip_id' in request_body:
            try:
                user_model = User.objects.get(username = request_body['username'])
                trip_model = Trip.objects.get(trip_id = request_body['trip_id'])
                user_model.favourite_trips.append(trip_model)
                user_model.save()
                return Response({'Added favourite trip'}, status=200)
            except DoesNotExist:
                return Response({'Given trip or user does not exist'}, status=400)
        else:
            return Response({'Missing username or trip'}, status=400)

class GetUser(MethodView):
    def get(self):
        request_id = request.headers.get('user_id')

        if request_id:
            try:
                user_model = User.objects.get(user_id = request_id)
                return jsonify(json.loads(user_model.to_json()))
            except DoesNotExist:
                return Response({'Given user does not exist'}, status=400)

class TripsHistory(MethodView):
    def post(self):
        request_body = request.get_json()

        if 'username' in request_body and 'trip_id' in request_body:
            try:
                user_model = User.objects.get(username = request_body['username'])
                trip_model = Trip.objects.get(trip_id = request_body['trip_id'])
                user_model.trip_history.append(trip_model)
                user_model.save()
                return Response({'Added favourite trip'}, status=200)
            except DoesNotExist:
                return Response({'Given trip or user does not exist'}, status=400)
        else:
            return Response({'Missing username or trip'}, status=400)

class LoginUser(MethodView):
    def post(self):
        request_body = request.get_json()
        print(request_body)
        if not 'username' in request_body and not 'password' in request_body:
            return Response({'Missing username or password'}, status=400)
        try:
            user_model = User.objects.get(username = request_body['username'])
            if request_body['password'] == user_model.password:
                user_model.start_session()
                return jsonify(json.loads(user_model.to_json()))
            else:
                return Response({'Wrong username or password'}, status=400)
        except DoesNotExist:
            return Response({'Wrong username or password'}, status=400)
    
user_bp.add_url_rule('/user/register', view_func=RegisterUser.as_view('register'), methods=['POST'])
user_bp.add_url_rule('/user/trips/fav', view_func=TripsFavourite.as_view('fav_trip'), methods=['POST'])
user_bp.add_url_rule('/user/trips/history', view_func=TripsHistory.as_view('history_trip'), methods=['POST'])
user_bp.add_url_rule('/user/login', view_func=LoginUser.as_view('login'), methods=['POST'])
user_bp.add_url_rule('/user/get', view_func=GetUser.as_view('get_user'), methods=['GET'])

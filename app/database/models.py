from enum import unique
from mongoengine import Document
from mongoengine import DateTimeField, StringField, ReferenceField, IntField, FloatField

class City(Document):
    city_id = IntField(primary_key=True)
    name = StringField(max_length=255, unique=True, required=True)

    def __repr__(self):
        return self.city_id + ' ' + self.name

class Route(Document):
    route_id = StringField(max_lenght=10, primary_key=True)
    short_name = StringField(max_lenght=50)
    description = StringField(max_lenght=255)

    def __repr__(self):
        return self.route_id + ' ' + self.short_name + ' ' + self.description

class Stop(Document):
    stop_id = IntField(primary_key=True)
    code = IntField()
    name = StringField(255)
    latitude = FloatField()
    longitude = FloatField()

    def __repr__(self):
        return self.stop_id + ' ' + self.code + ' ' + self.name

class Trip(Document):
    route = ReferenceField(Route)
    service_id = IntField()
    trip_id = StringField(max_length=20, primary_key=True)
    trip_headsign = StringField(255)
    direction_id = IntField()

    def __repr__(self):
        return self.trip_id + ' ' + self.route_id + ' ' + self.trip_headsign + ' ' + self.direction_id

class StopTimes(Document):
    trip = ReferenceField(Trip)
    stop = ReferenceField(Stop)
    departure_time = DateTimeField()

    def __repr__(self):
        return self.trip.trip_id + ' ' + self.stop_id + ' ' + self.departure_time
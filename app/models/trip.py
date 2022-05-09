from mongoengine import Document
from mongoengine import StringField, ReferenceField, IntField, FloatField

from app.models.route import Route

class Trip(Document):
    route = ReferenceField(Route)
    service_id = IntField()
    trip_id = StringField(primary_key=True)
    trip_headsign = StringField()
    direction_id = IntField()
    meta = {'collection': 'mpk-trips'}
    
    def __repr__(self):
        return self.trip_id + ' ' + self.route_id + ' ' + self.trip_headsign + ' ' + self.direction_id
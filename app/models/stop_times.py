from mongoengine import Document
from mongoengine import DateTimeField, ReferenceField

from app.models.trip import Trip
from app.models.stop import Stop

class StopTimes(Document):
    trip = ReferenceField(Trip)
    stop = ReferenceField(Stop)
    departure_time = DateTimeField()
    meta = {'collection': 'mpk-stop-times'}

    def __repr__(self):
        return self.trip.trip_id + ' ' + self.stop_id + ' ' + self.departure_time
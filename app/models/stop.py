from mongoengine import Document
from mongoengine import StringField, IntField, PointField

class Stop(Document):
    stop_id = IntField(primary_key=True)
    code = IntField()
    name = StringField()
    lat_lon = PointField()
    meta = {'collection': 'mpk-stops'}

    def __repr__(self):
        return self.stop_id + ' ' + self.code + ' ' + self.name
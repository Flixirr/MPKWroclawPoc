from mongoengine import Document
from mongoengine import StringField, IntField

class City(Document):
    city_id = IntField(primary_key=True)
    name = StringField(max_length=255, unique=True, required=True)
    meta = {'collection': 'mpk-cities'}

    def __repr__(self):
        return self.city_id + ' ' + self.name
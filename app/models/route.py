from mongoengine import Document
from mongoengine import StringField

class Route(Document):
    route_id = StringField(max_lenght=10, primary_key=True)
    short_name = StringField()
    description = StringField()
    meta = {'collection': 'mpk-routes'}
    
    def __repr__(self):
        return self.route_id + ' ' + self.short_name + ' ' + self.description
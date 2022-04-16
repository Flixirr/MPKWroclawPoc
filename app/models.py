from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from flask_appbuilder import Model

class City(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique = True, nullable=False)

    def __repr__(self):
        return self.id + ' ' + self.name

class Route(Model):
    id = Column(String(10), primary_key=True)
    short_name = Column(String(50))
    description = Column(String(255))

    def __repr__(self):
        return self.id + ' ' + self.short_name + ' ' + self.description

class Stop(Model):
    id = Column(Integer, primary_key=True)
    code = Column(Integer)
    name = Column(String(255))
    latitude = Column(Float)
    longitude = Column(Float)

    def __repr__(self):
        return self.id + ' ' + self.code + ' ' + self.name

class Trip(Model):
    route_id = Column(String(10), ForeignKey('route.id'))
    service_id = Column(Integer, )

class StopTimes(Model):
    id = Column
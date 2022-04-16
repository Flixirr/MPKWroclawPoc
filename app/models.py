from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from flask_appbuilder import Model

class City(Model):
    city_id = Column(Integer, primary_key=True)
    name = Column(String(50), unique = True, nullable=False)

    def __repr__(self):
        return self.city_id + ' ' + self.name

class Route(Model):
    route_id = Column(String(10), primary_key=True)
    short_name = Column(String(50))
    description = Column(String(255))

    def __repr__(self):
        return self.route_id + ' ' + self.short_name + ' ' + self.description

class Stop(Model):
    stop_id = Column(Integer, primary_key=True)
    code = Column(Integer)
    name = Column(String(255))
    latitude = Column(Float)
    longitude = Column(Float)

    def __repr__(self):
        return self.stop_id + ' ' + self.code + ' ' + self.name

class Trip(Model):
    route_id = Column(String(10), ForeignKey('route.route_id'))
    route = relationship("Route")
    service_id = Column(Integer)
    trip_id = Column(String(20), primary_key=True)
    trip_headsign = Column(String(255))
    direction_id = Column(Integer)

    def __repr__(self):
        return self.trip_id + ' ' + self.route_id + ' ' + self.trip_headsign + ' ' + self.direction_id

class StopTimes(Model):
    trip_id = Column(String(20), ForeignKey('trip.trip_id'))
    trip = relationship("Trip")
    stop_id = Column(Integer, ForeignKey('stop.stop_id'))
    stop = relationship("Stop")
    departure_time = Column(DateTime)

    def __repr__(self):
        return self.trip_id + ' ' + self.stop_id + ' ' + self.departure_time
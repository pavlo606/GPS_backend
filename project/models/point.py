from .i_dto import IDto
from project import db

class Point(db.Model, IDto):
    id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.DECIMAL(9, 6), nullable=False)
    lon = db.Column(db.DECIMAL(9, 6), nullable=False)
    datatime = db.Column(db.TIMESTAMP, nullable=False)

    route_id = db.Column(db.Integer, db.ForeignKey('route.id'), nullable=False)
    
    def put_into_dto(self):
        return {
            'id': self.id,
            'lat': self.lat,
            'lon': self.lon,
            'datatime': str(self.datatime),
            'route_id': self.route_id
        }
from .i_dto import IDto
from project import db

class Route(db.Model, IDto):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
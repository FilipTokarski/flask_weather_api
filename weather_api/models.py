from datetime import datetime
from weather_api import db

class Cities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(50), nullable=False)
    temp = db.Column(db.String(10), nullable=False)
    icon = db.Column(db.String(10), nullable=False)
    weather = db.Column(db.String(50), nullable=False)
    date = db.Column(db.DateTime(timezone=True),
                     nullable=False, 
                     default=datetime.now)

    def __repr__(self):
        return self.city

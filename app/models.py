from app import db
from datetime import datetime


class Note(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(140), index=True, unique=True)
	text = db.Column(db.String(10000))
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	
	def __repr__(self):
		return '<Note {}>'.format(self.name)


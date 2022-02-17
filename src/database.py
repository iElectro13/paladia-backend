from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    category = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    image = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    seller = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())

    def __repr__(self) -> str:
        return "User >>> {self.username}"

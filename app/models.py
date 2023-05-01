from app import db
from datetime import datetime

class Showcase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    name_cn = db.Column(db.String(50))
    author = db.Column(db.String(50))
    author_cn = db.Column(db.String(50))
    description = db.Column(db.Text)
    image = db.Column(db.String(100))
    video = db.Column(db.String(100))
    project_url = db.Column(db.String(100))
    service_url = db.Column(db.String(100))
    blog_url = db.Column(db.String(100))
    weight = db.Column(db.Integer)
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime, default=datetime.utcnow)

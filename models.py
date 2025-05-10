from datetime import datetime
from extensions import db


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    excerpt = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    comments = db.relationship('Comment', backref='post', lazy=True)
    image_url = db.Column(db.String(200), nullable=True)


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=False)
    username = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    event_date = db.Column(db.DateTime, nullable=False)
    image_url = db.Column(db.String(120), nullable=False,
                          default='default_event.jpg')
    link = db.Column(db.String(200), nullable=False)
    is_featured = db.Column(db.Boolean, default=False)
    category = db.Column(db.String(50), default='Conference')

    def __repr__(self):
        return f"Event('{self.title}', '{self.event_date}', '{self.location}')"

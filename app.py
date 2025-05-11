from flask import Flask, render_template, url_for, request, redirect, jsonify
import random
from extensions import db
from flask_migrate import Migrate
from models import Post, Comment, Event
from datetime import datetime
import os


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'DATABASE_URL', 'sqlite:///site.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate = Migrate(app, db)

    # Initialize the database if needed
    with app.app_context():
        try:
            # Try to query the database
            Event.query.first()
        except Exception as e:
            print(f"Database initialization needed: {e}")
            db.create_all()
            print("Database tables created successfully!")

    @app.context_processor
    def inject_year():
        return {'year': datetime.utcnow().year}

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/contact')
    def contact():
        return render_template('contact.html')

    @app.route('/api/events')
    def get_events():
        try:
            events = Event.query.all()
            events_data = [
                {
                    "title": event.title,
                    "start": event.event_date.strftime('%Y-%m-%d'),
                    "url": event.link
                }
                for event in events
            ]
            return jsonify(events_data)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route('/')
    def home():
        teaser_events = Event.query.filter_by(is_featured=True).order_by(
            Event.event_date.asc()).limit(2).all()
        return render_template('index.html', teaser_events=teaser_events)

    @app.route('/events')
    def events():
        featured_events = Event.query.filter_by(
            is_featured=True).order_by(Event.event_date).all()
        all_events = Event.query.order_by(Event.event_date).all()
        return render_template('events.html', featured_events=featured_events, events=all_events)

    @app.route("/blogs")
    def blogs():
        posts = Post.query.all()
        featured_post = random.choice(posts) if posts else None
        return render_template("blogs.html", posts=posts, featured_post=featured_post)

    @app.route("/post/<int:post_id>")
    def post(post_id):
        post = Post.query.get_or_404(post_id)
        comments = Comment.query.filter_by(post_id=post.id).all()

        # Get previous and next posts for navigation
        prev_post = Post.query.filter(
            Post.id < post_id).order_by(Post.id.desc()).first()
        next_post = Post.query.filter(
            Post.id > post_id).order_by(Post.id.asc()).first()

        related_posts = Post.query.filter(
            Post.category == post.category,
            Post.id != post.id
        ).order_by(Post.date_posted.desc()).limit(3).all()

        return render_template("post.html", post=post, comments=comments,
                               prev_post=prev_post, next_post=next_post,
                               related_posts=related_posts)

    @app.route('/add_comment/<int:post_id>', methods=['POST'])
    def add_comment(post_id):
        username = request.form.get('username')
        body = request.form.get('content')

        comment = Comment(
            username=username,
            body=body,
            post_id=post_id,
            date_posted=datetime.utcnow()
        )

        db.session.add(comment)
        db.session.commit()

        # Redirect to the post page
        return redirect(url_for('post', post_id=post_id))

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

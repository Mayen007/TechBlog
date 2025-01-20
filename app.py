from flask import Flask, render_template, url_for, request, redirect
import random
from extensions import db
from flask_migrate import Migrate
from models import Post, Comment
from datetime import datetime


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comments.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate = Migrate(app, db)

    @app.context_processor
    def inject_year():
        return {'year': datetime.utcnow().year}

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/contact')
    def contact():
        return render_template('contact.html')

    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/blogs")
    def blogs():
        posts = Post.query.all()
        featured_post = random.choice(posts)
        return render_template("blogs.html", posts=posts, featured_post=featured_post)

    @app.route("/post/<int:post_id>")
    def post(post_id):
        post = Post.query.get_or_404(post_id)
        comments = Comment.query.filter_by(post_id=post.id).all()
        return render_template("post.html", post=post, comments=comments)


    @app.route('/add_comment/<int:post_id>', methods=['POST'])
    def add_comment(post_id):
        # Correctly fetch the form data using parentheses
        username = request.form.get('username')
        content = request.form.get('content')
    
        # Create a new comment object
        comment = Comment(
        username=username,
        content=content,
        post_id=post_id,
        date_posted=datetime.utcnow()
    )
    
         # Add the comment to the database
        db.session.add(comment)
        db.session.commit()
    
        # Redirect to the post page
        return redirect(url_for('post', post_id=post_id))

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

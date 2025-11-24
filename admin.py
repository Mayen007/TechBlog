from dotenv import load_dotenv
import os
from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from urllib.parse import urlparse
from functools import wraps
from werkzeug.security import check_password_hash, generate_password_hash
from extensions import db
from models import Post, Event, Comment
from datetime import datetime

admin = Blueprint('admin', __name__, url_prefix='/admin')

# Admin authentication

# Load environment variables from a .env file (if present)
load_dotenv()

# Admin credentials
# `ADMIN_PASSWORD` should be a hashed password (use `generate_password.py` to create one).
ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME', 'admin')
# expected to be a hashed password
ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD')


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin_logged_in' not in session:
            return redirect(url_for('admin.login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


@admin.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # If ADMIN_PASSWORD is not configured, prevent login and notify.
        if not ADMIN_PASSWORD:
            flash(
                'Admin password not configured. Set `ADMIN_PASSWORD` in your environment.', 'danger')
            return render_template('admin/login.html')

        if username == ADMIN_USERNAME and check_password_hash(ADMIN_PASSWORD, password):
            session['admin_logged_in'] = True
            flash('Login successful!', 'success')
            next_page = request.args.get('next', url_for('admin.dashboard'))
            next_page_stripped = next_page.replace('\\', '')
            parsed = urlparse(next_page_stripped)
            if not parsed.scheme and not parsed.netloc:
                return redirect(next_page_stripped)
            else:
                return redirect(url_for('admin.dashboard'))
        else:
            flash('Invalid credentials', 'danger')

    return render_template('admin/login.html')


@admin.route('/logout')
def logout():
    session.pop('admin_logged_in', None)
    flash('You have been logged out', 'success')
    return redirect(url_for('admin.login'))


@admin.route('/')
@login_required
def dashboard():
    posts_count = Post.query.count()
    events_count = Event.query.count()
    comments_count = Comment.query.count()

    recent_posts = Post.query.order_by(Post.date_posted.desc()).limit(5).all()
    recent_comments = Comment.query.order_by(
        Comment.date_posted.desc()).limit(5).all()

    return render_template('admin/dashboard.html',
                           posts_count=posts_count,
                           events_count=events_count,
                           comments_count=comments_count,
                           recent_posts=recent_posts,
                           recent_comments=recent_comments)

# Post management routes


@admin.route('/posts')
@login_required
def posts():
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    return render_template('admin/posts.html', posts=posts)


@admin.route('/posts/new', methods=['GET', 'POST'])
@login_required
def new_post():
    if request.method == 'POST':
        title = request.form.get('title')
        excerpt = request.form.get('excerpt')
        content = request.form.get('content')
        category = request.form.get('category')
        image_url = request.form.get('image_url')

        if not title or not content or not excerpt:
            flash('Title, excerpt, and content are required', 'danger')
            return render_template('admin/post_form.html')

        post = Post(
            title=title,
            excerpt=excerpt,
            content=content,
            category=category,
            image_url=image_url
        )

        db.session.add(post)
        db.session.commit()

        flash('Post created successfully!', 'success')
        return redirect(url_for('admin.posts'))

    return render_template('admin/post_form.html')


@admin.route('/posts/<int:post_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)

    if request.method == 'POST':
        post.title = request.form.get('title')
        post.excerpt = request.form.get('excerpt')
        post.content = request.form.get('content')
        post.category = request.form.get('category')
        post.image_url = request.form.get('image_url')

        db.session.commit()
        flash('Post updated successfully!', 'success')
        return redirect(url_for('admin.posts'))

    return render_template('admin/post_form.html', post=post)


@admin.route('/posts/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)

    # Delete related comments
    Comment.query.filter_by(post_id=post_id).delete()

    db.session.delete(post)
    db.session.commit()

    flash('Post deleted successfully!', 'success')
    return redirect(url_for('admin.posts'))

# Event management routes


@admin.route('/events')
@login_required
def events():
    events = Event.query.order_by(Event.event_date.desc()).all()
    return render_template('admin/events.html', events=events)


@admin.route('/events/new', methods=['GET', 'POST'])
@login_required
def new_event():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        location = request.form.get('location')
        event_date = request.form.get('event_date')
        image_url = request.form.get('image_url')
        link = request.form.get('link')
        category = request.form.get('category')
        is_featured = 'is_featured' in request.form

        if not title or not description or not location or not event_date or not link:
            flash('Please fill all required fields', 'danger')
            return render_template('admin/event_form.html')

        event = Event(
            title=title,
            description=description,
            location=location,
            event_date=datetime.strptime(event_date, '%Y-%m-%d'),
            image_url=image_url,
            link=link,
            category=category,
            is_featured=is_featured
        )

        db.session.add(event)
        db.session.commit()

        flash('Event created successfully!', 'success')
        return redirect(url_for('admin.events'))

    return render_template('admin/event_form.html')


@admin.route('/events/<int:event_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_event(event_id):
    event = Event.query.get_or_404(event_id)

    if request.method == 'POST':
        event.title = request.form.get('title')
        event.description = request.form.get('description')
        event.location = request.form.get('location')
        event.event_date = datetime.strptime(
            request.form.get('event_date'), '%Y-%m-%d')
        event.image_url = request.form.get('image_url')
        event.link = request.form.get('link')
        event.category = request.form.get('category')
        event.is_featured = 'is_featured' in request.form

        db.session.commit()
        flash('Event updated successfully!', 'success')
        return redirect(url_for('admin.events'))

    return render_template('admin/event_form.html', event=event)


@admin.route('/events/<int:event_id>/delete', methods=['POST'])
@login_required
def delete_event(event_id):
    event = Event.query.get_or_404(event_id)

    db.session.delete(event)
    db.session.commit()

    flash('Event deleted successfully!', 'success')
    return redirect(url_for('admin.events'))

# Comment management routes


@admin.route('/comments')
@login_required
def comments():
    comments = Comment.query.order_by(Comment.date_posted.desc()).all()
    return render_template('admin/comments.html', comments=comments)


@admin.route('/comments/<int:comment_id>/delete', methods=['POST'])
@login_required
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)

    db.session.delete(comment)
    db.session.commit()

    flash('Comment deleted successfully!', 'success')
    return redirect(url_for('admin.comments'))

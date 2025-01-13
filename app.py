from flask import Flask, render_template, url_for
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    current_year = datetime.now().year
    return render_template('index.html', year=current_year)


@app.route('/about')
def about():
    current_year = datetime.now().year
    return render_template('about.html', year=current_year)


@app.route('/blogs')
def blogs():
    current_year = datetime.now().year
    return render_template('blogs.html', year=current_year)


@app.route('/contact')
def contact():
    current_year = datetime.now().year
    return render_template('contact.html', year=current_year)


@app.route('/blog/<int:post_id>')
def blog(post_id):
    current_year = datetime.now().year
    try:
        return render_template(f'post{post_id}.html', year=current_year)
    except:
        return "Post not found", 404


if __name__ == '__main__':
    app.run(debug=True)

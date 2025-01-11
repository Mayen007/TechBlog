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


@app.route('/blog1')
def blog1():
    current_year = datetime.now().year
    return render_template('post1.html', year=current_year)


@app.route('/blog2')
def blog2():
    current_year = datetime.now().year
    return render_template('post2.html', year=current_year)


@app.route('/blog4')
def blog4():
    current_year = datetime.now().year
    return render_template('post4.html', year=current_year)


if __name__ == '__main__':
    app.run(debug=True)

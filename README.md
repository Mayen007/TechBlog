# TechBlog

TechBlog is a modern, sleek tech-focused website designed to keep users updated on the latest trends, news, and insights in the world of technology. Built with Flask, HTML, CSS, and JavaScript, this site provides a seamless user experience with features like a dynamic event calendar, category filtering, and a responsive layout optimized for all devices.

## Live Demo

Check out the live site here:

- [TechBlog on Vercel](https://techblog-b0bw0y966-mayens-projects.vercel.app)
- [TechBlog on Render](https://tech-blog-t04y.onrender.com)

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Tech Stack](#tech-stack)
- [Contributing](#contributing)
- [Code of Conduct](#code-of-conduct)
- [Issues](#issues)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features

- **Responsive Design**: Fully optimized for all screen sizes, including desktops, tablets, and smartphones.
- **Dark/Light Theme Toggle**: User-controlled theme preference that persists across sessions.
- **Dynamic Event Calendar**: Browse and filter tech events by category (Conferences, Workshops, Webinars, Hackathons).
- **Blog Post Filtering**: Find articles by category with interactive filtering.
- **Related Articles**: Smart suggestions for related content based on the current post's category.
- **Post Navigation**: Easy navigation between previous and next posts.
- **Comment System**: Leave comments on blog posts with real-time submission.
- **Sleek Navigation**: Sticky header with a navigation bar that collapses into a mobile-friendly menu.

## Installation

### Prerequisites

To run this project, ensure you have the following installed:

- Python 3.x
- Flask
- Virtual environment (optional but recommended)

### Clone the Repository

```bash
git clone https://github.com/mayen007/TechBlog.git
cd TechBlog
```

### Set Up Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Initialize the Database

```bash
python populate_db.py
```

### Run the Application

```bash
flask run
```

The application will be available at `http://127.0.0.1:5000/`.

### Deployment

#### Deploy to Vercel:

```bash
vercel login
vercel
```

#### Deploy to Render:

Create a new Web Service on Render, connect your GitHub repository, and set:

- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app`

## Tech Stack

- **Flask** - Backend web framework.
- **SQLAlchemy** - ORM for database management.
- **Flask-Migrate** - Database migrations.
- **HTML5** - For structuring content.
- **CSS3** - Styled with modern CSS techniques including CSS variables for theming.
- **JavaScript (ES6+)** - For interactive features like filtering and theme toggling.
- **FontAwesome** - Icons used throughout the site.
- **Gunicorn** - WSGI HTTP Server for deployment.
- **Vercel & Render** - Hosting platforms for deployment.

## Contributing

We welcome contributions to improve TechBlog! To contribute:

1. Fork the repository.
2. Create a new branch for your feature:

   ```bash
   git checkout -b feature-name
   ```

3. Make your changes and commit:

   ```bash
   git commit -m "Add new feature"
   ```

4. Push to your branch:

   ```bash
   git push origin feature-name
   ```

5. Open a pull request describing your changes.

### Contribution Guidelines

- Ensure your code follows best practices and is well-documented.
- Keep pull requests small and focused on one feature/fix at a time.
- Check for open issues before starting new features.
- Be respectful and constructive in discussions.

## Code of Conduct

By contributing to TechBlog, you agree to follow our [Code of Conduct](CODE_OF_CONDUCT.md) to foster an open and welcoming environment.

## Issues

If you find a bug or have a feature request, please check the [issues](https://github.com/mayen007/TechBlog/issues) tab or create a new issue with a clear description.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to the open-source community for providing inspiration and code snippets.
- Icons provided by FontAwesome.
- High-quality images sourced from [Freepik](https://www.freepik.com) and [Unsplash](https://unsplash.com).
- Deployed on [Vercel](https://vercel.com) and [Render](https://render.com) platforms.

## Project Structure

```
TechBlog/
├── app.py                # Main application file
├── extensions.py         # Flask extensions
├── models.py             # Database models
├── populate_db.py        # Database initialization
├── requirements.txt      # Dependencies
├── vercel.json           # Vercel deployment configuration
├── static/               # Static assets
│   ├── css/              # Stylesheets
│   ├── img/              # Images
│   └── js/               # JavaScript files
└── templates/            # HTML templates
    ├── base.html         # Base template
    ├── index.html        # Homepage
    ├── blogs.html        # Blog listing
    ├── post.html         # Single blog post
    ├── events.html       # Events listing
    ├── about.html        # About page
    └── contact.html      # Contact page
```

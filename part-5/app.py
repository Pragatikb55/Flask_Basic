"""
Part 5: Mini Project - Personal Website with Flask
===================================================
A complete personal website using everything learned in Parts 1-4.

How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Open browser: http://localhost:5000
"""

from multiprocessing.util import info
from flask import Flask, render_template

app = Flask(__name__)

# =============================================================================
# YOUR DATA - Customize this section with your own information!
# =============================================================================

PERSONAL_INFO = {
    'name': 'Pragati Kshirsagar',
    'title': 'Web Developer',
    'bio': 'A passionate developer learning Flask and web development.',
    'email': 'pragatik194@example.com',
    'github': 'https://github.com/Pragatikb55',
}

SKILLS = [
    {'name': 'Python', 'level': 85, 'slug': 'python'},
    {'name': 'HTML/CSS', 'level': 80, 'slug': 'html-css'},
    {'name': 'Flask', 'level': 75, 'slug': 'flask'},
    {'name': 'JavaScript', 'level': 30, 'slug': 'javascript'},
    {'name': 'SQL', 'level': 50, 'slug': 'sql'},
    {'name': 'DBMS', 'level': 80, 'slug': 'dbms'},
]

PROJECTS = [
    {'id': 1, 'name': 'Personal Website', 'description': 'A Flask-powered personal portfolio website.', 'tech': ['Python', 'Flask', 'HTML', 'CSS'], 'status': 'Completed'},
    {'id': 2, 'name': 'News agregated bot', 'description': 'A Telegram bot that collects and delivers news from multiple RSS sources based on user preferences.', 'tech':['Python', 'python-telegram-bot', 'SQLite', 'RSS'], 'status': 'Completed'},
    {'id': 3, 'name': 'Catchyour vehicle', 'description':'A vehicle tracking and management system for monitoring vehicle details and status.', 'tech': ['Python', 'Flask', 'HTML', 'CSS', 'SQLite'], 'status': 'In Progress'},
]


# =============================================================================
# ROUTES
# =============================================================================


# Blog posts data
BLOG_POSTS = [
    {
        "title": "Building My Personal Website with Flask",
        "author": "Pragati Kshirsagar",
        "content": (
            "This project is a Flask-powered personal portfolio website. "
            "It includes sections like About Me, Skills, Projects, and Contact. "
            "I learned how to use Jinja2 templates, dynamic routing, and CSS styling."
        )
    },
    {
        "title": "News Aggregated Telegram Bot Using Python",
        "author": "Pragati Kshirsagar",
        "content": (
            "This project is a Telegram bot that collects news from multiple RSS sources. "
            "Users can choose categories, and news is delivered automatically. "
            "The bot is built using Python, python-telegram-bot, and SQLite."
        )
    },
    {
        "title": "Catch Your Vehicle – Vehicle Management System",
        "author": "Pragati Kshirsagar",
        "content": (
            "Catch Your Vehicle is a vehicle tracking and management system. "
            "It helps in storing and monitoring vehicle details efficiently. "
            "This project strengthened my understanding of Flask, databases, and backend logic."
        )
    }
]

@app.route('/')
def home():
    return render_template('index.html', info=PERSONAL_INFO)


@app.route('/about')
def about():
    return render_template('about.html', info=PERSONAL_INFO, skills=SKILLS)


@app.route('/projects')
def projects():
    return render_template('projects.html', info=PERSONAL_INFO, projects=PROJECTS)


@app.route('/project/<int:project_id>')  # Dynamic route for individual project
def project_detail(project_id):
    project = None
    for p in PROJECTS:
        if p['id'] == project_id:
            project = p
            break
    return render_template('project_detail.html', info=PERSONAL_INFO, project=project, project_id=project_id)


@app.route('/contact')
def contact():
    return render_template('contact.html', info=PERSONAL_INFO)

@app.route('/blog')
def blog():
    return render_template('blog.html', info=PERSONAL_INFO, posts=BLOG_POSTS)

@app.route('/skill/<slug>')
def skill_projects(slug):
    filtered_projects = [
        project for project in PROJECTS
        if any(
            slug.replace('-', '').lower() in tech.replace('/', '').lower()
            for tech in project['tech']
        )
    ]

    skill_name = slug.replace('-', '/').upper()

    return render_template(
        'skill.html',
        info=PERSONAL_INFO,
        skill_name=skill_name,
        projects=filtered_projects
    )


if __name__ == '__main__':
    app.run(debug=True)


# =============================================================================
# PROJECT STRUCTURE:
# =============================================================================
#
# part-5/
# ├── app.py              <- You are here
# ├── static/
# │   └── style.css       <- CSS styles
# └── templates/
#     ├── base.html       <- Base template (inherited by all pages)
#     ├── index.html      <- Home page
#     ├── about.html      <- About page
#     ├── projects.html   <- Projects list
#     ├── project_detail.html <- Single project view
#     └── contact.html    <- Contact page
#
# =============================================================================

# =============================================================================
# EXERCISES:
# =============================================================================
#
# Exercise 5.1: Personalize your website
#   - Update PERSONAL_INFO with your real information
#   - Add your actual skills and projects
#
# Exercise 5.2: Add a new page
#   - Create a /blog route
#   - Add blog posts data structure
#   - Create blog.html template
#
# Exercise 5.3: Enhance the styling
#   - Modify static/style.css
#   - Add your own color scheme
#   - Make it responsive for mobile
#
# Exercise 5.4: Add more dynamic features
#   - Create a /skill/<skill_name> route
#   - Show projects that use that skill
#
# =============================================================================

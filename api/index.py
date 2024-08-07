from flask import Flask, render_template
import os

# Adjust the template and static folder paths
app = Flask(__name__, template_folder='../templates', static_folder='../static')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/lesson/python-basics')
def python_basics():
    return render_template('lesson.html', lesson_title="Python Basics", lesson_content="Here's where you'd put your lesson content.")

# This is for Vercel serverless
def handler(request, response):
    return app(request, response)

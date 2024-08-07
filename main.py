from flask import Flask, render_template

app = Flask(__name__)

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

# Remove the if __name__ == '__main__': block entirely

# Add this line at the end of the file
app = app

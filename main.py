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

# Add more routes for additional pages or functionalities as needed

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Vercel, 
    # Vercel runs the app directly, so this block is not executed.
    app.run(host='0.0.0.0', port=8080)

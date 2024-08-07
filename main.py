from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask!"

# This line is important for Vercel
app = app

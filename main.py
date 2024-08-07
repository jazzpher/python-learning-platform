from flask import Flask
from flask.helpers import make_response

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask!"

# This is the handler for Vercel serverless functions
def handler(request):
    return make_response(app.handle_request())

# Keep this line
app = app

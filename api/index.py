from flask import Flask, Request
from flask.helpers import make_response

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask!"

def handler(request: Request):
    with app.request_context(request.environ):
        return make_response(app.handle_request())

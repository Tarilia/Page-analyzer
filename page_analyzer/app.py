from flask import Flask


app = Flask(__name__)

@app.route('/')
def get_hello():
    return 'Hello! There will be a page analyzer here.'

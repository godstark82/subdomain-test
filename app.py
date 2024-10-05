from flask import Flask

app = Flask(__name__)

@app.route('/<subdomain>', subdomain='<subdomain>')
def index(subdomain):
    return 'Hello, World! ' + subdomain

@app.route('/')
def index():
    return 'Hello, World!'



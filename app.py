from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<subdomain>', subdomain='<subdomain>')
def index(subdomain):
    return 'Hello, World! ' + subdomain

@app.route('/')
def index():
    return render_template('index.html')



from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SERVER_NAME'] = 'subdomain-test-phi.vercel.app'

@app.route('/', subdomain='<subdomain>')
def subdomain_route(subdomain):
    return f'Hello from subdomain: {subdomain}'

@app.route('/', defaults={'subdomain': None})
@app.route('/', subdomain='<subdomain>')
def index(subdomain):
    if subdomain:
        return f'Hello from subdomain: {subdomain}'
    return render_template('index.html')


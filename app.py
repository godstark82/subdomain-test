from flask import Flask, render_template

app = Flask(__name__)
app.config['SERVER_NAME'] = 'subdomain-test-phi.vercel.app/'

@app.route('/', subdomain='a')
def subdomain_route(subdomain):
    # Your function code here
    return 'Hello ' + subdomain

@app.route('/')
def index():
    return render_template('index.html')



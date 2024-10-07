from flask import Flask


# Hw8NYH8yYaInwwir4ZYz


app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True) # run the app



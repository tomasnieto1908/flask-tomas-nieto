from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/san lorenzo')
def Boca():
    return 'san lorenzo el mas grande de todos'
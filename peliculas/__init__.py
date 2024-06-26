from flask import Flask, render_template 

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/san lorenzo')
def Boca():
    return 'san lorenzo el mas grande de todos'

with app.app_context():
   from . import db
   db.init_app(app)

from . import actores
app.register_blueprint(actores.bp)

from . import lenguaje
app.register_blueprint(lenguaje.bp)

from . import pelicula
app.register_blueprint(pelicula.bp)
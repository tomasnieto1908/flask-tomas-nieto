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

@app.route('/actor')
def actor():
    consulta = """
        SELECT first_name, last_name FROM actor  
        ORDER BY first_name, last_name ASC
    """

    con = db.get_db()
    res = con.execute(consulta)
    lista_actores = res.fetchall()
    paginaActor = render_template("actor.html",
                              actores=lista_actores)
    return paginaActor



@app.route('/lenguaje')
def lenguaje():
    consulta = """
        SELECT name FROM language  
        ORDER BY name ASC
    """

    con = db.get_db()
    res = con.execute(consulta)
    lista_lenguaje = res.fetchall()
    paginalenguaje = render_template("lenguaje.html",
                              lenguajes=lista_lenguaje)
    return paginalenguaje
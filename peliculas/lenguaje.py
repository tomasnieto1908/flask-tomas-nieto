from flask import Blueprint, render_template
from . import db

bp = Blueprint('lenguaje', __name__, url_prefix='/lenguajes')

@db.route('/lenguaje')
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
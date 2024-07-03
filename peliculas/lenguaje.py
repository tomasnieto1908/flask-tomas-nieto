from flask import Blueprint, render_template
from . import db

bp = Blueprint('lenguaje', __name__, url_prefix="/lenguajes")

@bp.route('/')
def idioma():
    consulta = """
        SELECT name, language_id FROM language  
        ORDER BY name ASC
    """

    con = db.get_db()
    res = con.execute(consulta)
    lista_lenguajes = res.fetchall()
    paginaLenguaje = render_template("lenguaje.html",
                              lenguajes=lista_lenguajes)
    return paginaLenguaje

@bp.route('/<int:id>')
def detalle(id):
    consulta = """
        SELECT name, language_id FROM language
        WHERE language_id = ?
    """

    con = db.get_db()
    res = con.execute(consulta, (id,))
    lenguaje = res.fetchone()
    consulta2 = """
        SELECT 
    f.title AS titulo, 
    f.film_id
FROM 
    film f
WHERE 
    f.language_id = ?;

    """

    res = con.execute(consulta2, (id,))
    lista_peliculas = res.fetchall()
    paginaLenguaje = render_template("detalle_lenguaje.html",
                                  lenguaje=lenguaje,
                                  peliculas=lista_peliculas)
    return paginaLenguaje
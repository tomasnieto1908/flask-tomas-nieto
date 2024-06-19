from flask import Blueprint, render_template
from . import db

bp = Blueprint('actor', __name__, url_prefix='/actor')

@bp.route('/')
def actor():
    consulta = """
        SELECT first_name, last_name ,actor_id FROM actor  
        ORDER BY first_name, last_name ASC
    """

    con = db.get_db()
    res = con.execute(consulta)
    lista_actores = res.fetchall()
    paginaActor = render_template("actor.html",
                              actores=lista_actores)
    return paginaActor

@bp.route('/<int:id>')
def detalle(id):
    consulta = """
        SELECT first_name, last_name FROM actor  
        WHERE actor_id = ? 
    """

    con = db.get_db()
    res = con.execute(consulta, (id,))
    actor = res.fetchone()
    consulta2 = """
     SELECT title as titulo, f.film_id FROM film f
        JOIN film_actor fil on f.film_id = fil.film_id
        WHERE fil.actor_id = ?

    """

    res = con.execute(consulta2, (id,))
    lista_peliculas = res.fetchall()
    paginaActor = render_template("detalle_actor.html",
                              actor=actor,
                              peliculas=lista_peliculas)
    return paginaActor
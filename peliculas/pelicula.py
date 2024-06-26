from flask import Blueprint, render_template
from . import db

bp = Blueprint('Peliculas', __name__, url_prefix="/peliculas")

@bp.route('/')
def pelicula():
    consulta = """
        SELECT title, film_id FROM film
        ORDER BY title ASC
    """

    con = db.get_db()
    res = con.execute(consulta)
    lista_Peliculas = res.fetchall()
    paginaPelicula = render_template("pelicula.html",
                              peliculas=lista_Peliculas)
    return paginaPelicula


@bp.route('/<int:id>')
def detalle(id):
    consulta = """
          SELECT title, film_id FROM film

        WHERE film_id = ?
        ORDER BY title ASC
            """

    con = db.get_db()
    res = con.execute(consulta, (id,))
    pelicula = res.fetchone()
    consulta2 = """
           SELECT first_name, last_name, f.actor_id FROM film_actor f
        JOIN actor a ON a.actor_id = f.actor_id
        WHERE f.film_id = ?
    """

    res = con.execute(consulta2, (id,))
    lista_Actorespeliculas = res.fetchall()
    paginapelicula = render_template("detalle_pelicula.html",
                                  pelicula=pelicula,
                                  actores=lista_Actorespeliculas)
    return paginapelicula
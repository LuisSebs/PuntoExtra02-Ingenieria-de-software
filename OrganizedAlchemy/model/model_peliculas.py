from alchemyClasses.Pelicula import Pelicula

def get_all_peliculas():
    return Pelicula.query.all()

def get_pelicula_by_id(i):
    return Pelicula.query.get(i)

def get_pelicula_by_nombre(n):
    return Pelicula.query.filter_by(nombre=n)

def get_pelicula_by_genero(g):
    return Pelicula.query.filter(Pelicula.genero.like('%{}%'.format(g))).all()

def get_pelicula_by_menor_duracion(d):
    return Pelicula.query.filter(Pelicula.duracion < d).all()

def get_pelicula_by_mayor_duracion(d):
    return Pelicula.query.filter(Pelicula.duracion > d).all()

def get_pelicula_by_exacta_duracion(d):
    return Pelicula.query.filter(Pelicula.duracion == d).all()

def get_peliculas_disponibles():
    return Pelicula.query.filter(Pelicula.inventario > 0).all()
from alchemyClasses.Renta import Renta
from alchemyClasses import db
from model.model_peliculas import get_pelicula_by_id

def add_renta(idU, idP, ddr):
    
    # Agregamos la renta
    nueva_renta = Renta(idUsuario=idU, idPelicula=idP, dias_de_renta=ddr)
    db.session.add(nueva_renta)
    db.session.commit()

    # Reducimos el inventario de la pelicula
    pelicula = get_pelicula_by_id(idP)
    pelicula.inventario = pelicula.inventario - 1
    db.session.commit()


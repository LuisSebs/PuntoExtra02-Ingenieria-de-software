from alchemyClasses.Usuario import db
from model.model_usuario import get_all_users
from model.model_peliculas import get_all_peliculas
from model.model_peliculas import get_pelicula_by_id
from model.model_peliculas import get_pelicula_by_nombre
from model.model_peliculas import get_pelicula_by_genero
from model.model_peliculas import get_pelicula_by_menor_duracion
from model.model_peliculas import get_pelicula_by_mayor_duracion
from model.model_peliculas import get_pelicula_by_exacta_duracion
from model.model_peliculas import get_peliculas_disponibles
from model.model_usuario import get_usuario_by_id
from model.model_usuario import get_usuario_by_nombre
from model.model_usuario import get_usuario_by_correo
from model.model_renta import add_renta
from flask import Flask
from alchemyClasses.Usuario import Usuario
from utils.CryptoUtils import cipher
from hashlib import sha256

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://ferfong:Developer123!@localhost:3306/ing_soft"
app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)

menu = 'Seleccione una opcion:\n1)Ver usuarios\n2)Ver peliculas\n3)Registrar renta de pelicula\n4)Salir'
# eleccion_usuarios = 'Desea buscar por algun criterio?\n1)Si\n2)No'

def inserta_usuario(nombre, email, password):
    # pass_encryptada = sha256(cipher(password)).hexdigest()
    # nuevo_usuario = Usuario(nombre=nombre,email=email,passwd=pass_encryptada);
    print(sha256(cipher(password)).hexdigest())
    #  db.session.add(nuevo_usuario)

if __name__ == '__main__':

    with app.app_context():
        choice = 1
        while choice != 4:
            print(menu)
            choice = int(input())
            if choice == 1:
                menu1 = "[1] Todos los usuarios \n[2] Filtrar por id \n[3] Filtrar por nombre \n[4] Filtrar por correo \n[0] Regresar \n"
                while True:
                    print(menu1)
                    op = input("Ingresa una opcion: ")
                    if op == '0':
                        break;
                    elif op == '1':
                        for user in get_all_users():
                            print('===============')
                            print(user)
                            print('===============\n')
                    elif op == '2':
                        i = input("Ingresa el id del usuario: ")
                        print('===============')
                        print(get_usuario_by_id(int(i)))
                        print('===============\n')
                    elif op == '3':
                        n = input("Ingresa el nombre del usuario: ")
                        for user in get_usuario_by_nombre(n):
                            print('===============')
                            print(user)
                            print('===============\n')
                    elif op == '4':
                        c = input("Ingresa el correo del usuario: ")
                        for user in get_usuario_by_correo(c):
                            print('===============')
                            print(user)
                            print('===============\n')
                    else:
                        print("Ingresa una opcion valida")
            elif choice == 2:
                while True:
                    menu2 = "[1] Todas las peliculas \n[2] Filtrar por id \n[3] Filtrar por nombre \n[4] Filtrar por genero \n[5] Filtrar por duracion \n[0] Regresar \n"
                    print(menu2)
                    op = input("Ingresa una opcion: ")
                    if op == '0':
                        break;
                    elif op == '1':
                        for user in get_all_peliculas():
                            print('===============')
                            print(user)
                            print('===============\n')
                    elif op == '2':
                        i = input("Ingresa el id de la pelicula: ")
                        print('===============')
                        print(get_pelicula_by_id(int(i)))
                        print('===============\n')
                    elif op == '3':
                        n = input("Ingresa el nombre de la pelicula: ")
                        for user in get_pelicula_by_nombre(n):
                            print('===============')
                            print(user)
                            print('===============\n')
                    elif op == '4':
                        g = input("Ingresa el genero de la pelicula: ")
                        for user in get_pelicula_by_genero(g):
                            print('===============')
                            print(user)
                            print('===============\n')
                    elif op == '5':
                        while True:
                            print("[1] Menor a x duracion \n[2] Mayor a x duracion \n[3] Duracion exacta \n[0] Regresar \n")
                            op = input("Ingresa una opcion: ")
                            if op == '0':
                                break
                            elif op == '1':
                                d = input("Ingresa duracion: ")
                                for peli in get_pelicula_by_menor_duracion(int(d)):
                                    print('===============')
                                    print(peli)
                                    print('===============\n')
                            elif op == '2':
                                d = input("Ingresa duracion: ")
                                for peli in get_pelicula_by_mayor_duracion(int(d)):
                                    print('===============')
                                    print(peli)
                                    print('===============\n')
                            elif op == '3':
                                d = input("Ingresa duracion: ")
                                for peli in get_pelicula_by_exacta_duracion(int(d)):
                                    print('===============')
                                    print(peli)
                                    print('===============\n')
                            else:
                                print("Ingresa una opcion valida\n")
                    else:
                        print("Ingresa una opcion valida")
                for peli in get_all_peliculas():
                    print('===============')
                    print(peli)
                    print('===============\n')
            elif choice == 3:
                # Mostramos todas las peliculas  disponibles
                peliculas = get_peliculas_disponibles()
                if peliculas:
                    for pelicula in get_all_peliculas():
                        if pelicula.inventario > 0:
                            print(pelicula)
                else:
                    print("No tenemos peliculas disponibles :c, lo sentimos")
                    continue
                id_pelicula = int(input("Ingrese id pelicula: "))
                peli = get_pelicula_by_id(id_pelicula)
                if not peli:
                    print("Esa pelicula no existe")
                    continue

                # Mostramos todos los usuarios
                for usuario in get_all_users():
                    print(usuario)
                id_usuario = int(input("Ingrese id usuario: "))
                user = get_usuario_by_id(id_usuario)
                if not user:
                    print("Ese usuario no existe ")
                    continue
                
                # Verificamos que la pelicula este disponible
                if peli.inventario > 0:
                    # Generamos la renta
                    add_renta(user.idUsuario,peli.idPelicula,10)
                else:
                    print("Lo sentimos pero esa pelicula ya no esta disponible :c")
        else:
            print("Fin de sistema. :)")
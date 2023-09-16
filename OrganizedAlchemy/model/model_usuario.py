from alchemyClasses.Usuario import Usuario

def get_all_users():
    return Usuario.query.all()

def get_usuario_by_id(i):
    return Usuario.query.get(i)

def get_usuario_by_nombre(n):
    return Usuario.query.filter_by(nombre=n)

def get_usuario_by_correo(c):
    return Usuario.query.filter_by(email=c)

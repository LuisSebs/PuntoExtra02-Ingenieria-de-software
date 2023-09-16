# Punto Extra Práctica02

# Probar el punto extra

  - Favor de activar el entorno virtual

```bash
$ cd venv/

$ source Scripts/activate
 ```

- Favor de en MySQL Workbench ejecutar el script `PuntoExtra.sql` esto crea la base de datos, las tablas, he insertar a dos usuarios.

- Favor de posicionarse a la altura del archivo `app.py` y correrlo con el siguiente comando

```bash
$ python3 app.py
```

En caso de cualquier problema favor de contactarme.




# Proceso:

## Creacion de usuario y privilegios

**NOTA: Esta parte puede omitirse ya que el script `PuntoExtra.sql` ya crea el usuario y le da los privilegios**

Abrimos una terminal y accedemos a mysql con el usuario **root** he ingresamos la contraseña **root**

```bash
$ mysql -u root -p
```

Creamos el usuario `ferfong` con la contraseña `Developer123!` y le damos los permisos adecuados

```bash
$ create user 'ferfong'@'localhost' identified by 'Developer123!';

$ grant all privileges on *.* to 'ferfong'@'localhost';
```


## Correcciones al archivo `PuntoExtra.sql`

### 1.- Corregir el usuario

**Error: La especificación del usuario al que se le está otorgando los privilegios es incorrecta.**

Así es como están las primeras 4 lineas del script `PuntoExtra.sql`:

```sql
create database ing_soft;
use ing_soft;
create user 'ferfong'@'localhost' identified by 'Developer123!';
grant all privileges on ing_soft.* to 'ferfong';
```

Así tiene que quedar a continuación:

```sql
create database ing_soft;
use ing_soft;
create user 'ferfong'@'localhost' identified by 'Developer123!';
grant all privileges on ing_soft.* to 'ferfong'@'localhost'; -- Correccion
```
En caso de que hayas ejeuctado el script sin antes leer esta documentación, haz creado el usuario de `ferfong` pero no le has dado privilegios, esto puede traer complicaciones al correr todo el archivo una vez hayamos corregido los erroes, para eliminarlo desde mysql puedes realizar lo siguiente:

```sql
SELECT user FROM mysql.user;
```

Veras una tabla con todos los usuarios

```bash
+------------------+
| user             |
+------------------+
| debian-sys-maint |
| ferfong          |
| mysql.infoschema |
| mysql.session    |
| mysql.sys        |
| root             |
+------------------+
```

Eliminamos el usuario:

```sql
DROP user 'ferfong'@'localhost';
```

### 2.- Eliminar tabla repetida

**Error: Se tienen la creación de la tabla peliculas repetida**

Eliminar las lineas que crean de nuevo la tabla película

### 3.- Agregar la tabla Usuario

**Error: No se ha creado la tabla usuario**

Crear la tabla usuario (lo agregamos al script)

```sql
CREATE TABLE if not exists `usuarios` (
  `idUsuario` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  `email` varchar(500) DEFAULT NULL,
  `password` varchar(64) NOT NULL,
  `profilePicture` BLOB DEFAULT NULL,
  PRIMARY KEY (`idUsuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
```









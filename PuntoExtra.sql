create database if not exists ing_soft;
use ing_soft;
create user if not exists 'ferfong'@'localhost' identified by 'Developer123!';
grant all privileges on ing_soft.* to 'ferfong'@'localhost';
CREATE TABLE if not exists`peliculas` (
  `idPelicula` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  `genero` varchar(45) DEFAULT NULL,
  `duracion` int DEFAULT NULL,
  `inventario` int NOT NULL DEFAULT '1',
  PRIMARY KEY (`idPelicula`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE if not exists `usuarios` (
  `idUsuario` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  `email` varchar(500) DEFAULT NULL,
  `password` varchar(64) NOT NULL,
  `profilePicture` BLOB DEFAULT NULL,
  PRIMARY KEY (`idUsuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE if not exists`rentar` (
  `idRentar` int NOT NULL AUTO_INCREMENT,
  `idUsuario` int DEFAULT NULL,
  `idPelicula` int DEFAULT NULL,
  `fecha_renta` datetime NOT NULL,
  `dias_de_renta` int NOT NULL,
  `estatus` tinyint DEFAULT '0',
  PRIMARY KEY (`idRentar`),
  KEY `idUsuario_idx` (`idUsuario`),
  KEY `idPelicula_idx` (`idPelicula`),
  CONSTRAINT `idPelicula` FOREIGN KEY (`idPelicula`) REFERENCES `peliculas` (`idPelicula`),
  CONSTRAINT `idUsuario` FOREIGN KEY (`idUsuario`) REFERENCES `usuarios` (`idUsuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Peliculas
INSERT INTO peliculas (nombre, genero, duracion, inventario) VALUES ('toy story','animacion, aventura, infantil',80,2);
INSERT INTO peliculas (nombre, genero, duracion, inventario) VALUES ('shrek','aventura, fantasia, comedia',90,2);
INSERT INTO peliculas (nombre, genero, duracion, inventario) VALUES ('guardians of the galaxy vol.3','ciencia ficccion, accion',149,2);
INSERT INTO peliculas (nombre, genero, duracion, inventario) VALUES ('joker','crimen, drama',122,2);
INSERT INTO peliculas (nombre, genero, duracion, inventario) VALUES ('it','terror, suspenso',135,2);

-- Usuarios
INSERT INTO usuarios (nombre,email,password) VALUES ("Fer Fong","fernandofong@ciencias.unam.mx","e95fb3c63e1d451ba720d439f4a37f4059caf91233b451e8bc760aefa21be5b0");
INSERT INTO usuarios (nombre,email,password) VALUES ("Valeria Landa","vale@ciencias.unam.mx","51054d9eac78393dc2e063427598eeda04d5d5fec8e118fde9a39a557ff70586");

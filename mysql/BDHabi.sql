create database BDHabi;

create database BDHabi-character-set utf8

use BDHabi;


-- -----------------------------------------------------
-- Table propiedades
-- -----------------------------------------------------
DROP TABLE IF EXISTS propiedades ;

CREATE TABLE IF NOT EXISTS propiedades (
  idpropiedad INT NOT NULL AUTO_INCREMENT,
  estado VARCHAR(100) NOT NULL,
  ciudad VARCHAR(50) NOT NULL,
  colonia VARCHAR(50) NOT NULL,
  calle VARCHAR(250) NOT NULL,
  numero_exterior INT NOT NULL,
  tipo_inmueble VARCHAR(70) NOT NULL,
  transaccion VARCHAR(70) NOT NULL,
  precio DECIMAL NOT NULL,
  codigo_proveedor INT NOT NULL,
  telefono_contacto VARCHAR(45) NOT NULL,
  idusuario INT NOT NULL,
  PRIMARY KEY (idpropiedad)
)ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table usuarios
-- -----------------------------------------------------
DROP TABLE IF EXISTS usuarios ;


CREATE TABLE IF NOT EXISTS usuarios (
  idusuario INT NOT NULL AUTO_INCREMENT,
  correo_contacto VARCHAR(150) NOT NULL,
  PRIMARY KEY (idusuario)
)ENGINE = InnoDB;



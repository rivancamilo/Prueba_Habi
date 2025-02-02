use bdhabi;

--
-- Estructura de tabla para la tabla propiedades
--

CREATE TABLE propiedades (
  idpropiedad int(11) NOT NULL,
  estado varchar(100) NOT NULL,
  ciudad varchar(50) NOT NULL,
  colonia varchar(50) NOT NULL,
  calle varchar(250) DEFAULT NULL,
  numero_exterior varchar(50) DEFAULT NULL,
  tipo_inmueble varchar(70) NOT NULL,
  transaccion varchar(70) NOT NULL,
  precio decimal(10,0) NOT NULL,
  codigo_proveedor int(11) NOT NULL,
  telefono_contacto varchar(45) NOT NULL,
  idusuario int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;


--
-- Estructura de tabla para la tabla usuarios
--

CREATE TABLE usuarios (
  idusuario int(11) NOT NULL,
  correo_contacto varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;


--
-- Indices de la tabla propiedades
--
ALTER TABLE propiedades
  ADD PRIMARY KEY (idpropiedad),
  ADD KEY idusuario (idusuario);

--
-- Indices de la tabla usuarios
--
ALTER TABLE usuarios
  ADD PRIMARY KEY (idusuario);.


--
-- AUTO_INCREMENT de la tabla propiedades
--
ALTER TABLE propiedades
  MODIFY idpropiedad int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

--
-- AUTO_INCREMENT de la tabla usuarios
--
ALTER TABLE usuarios
  MODIFY idusuario int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1000;


--
-- Filtros para la tabla propiedades
--
ALTER TABLE propiedades
  ADD CONSTRAINT propiedades_ibfk_1 FOREIGN KEY (idusuario) REFERENCES usuarios (idusuario);
COMMIT;
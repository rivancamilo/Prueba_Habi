-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `idusuario` int(11) NOT NULL AUTO_INCREMENT,
  `correo_contacto` varchar(150) NOT NULL,
  PRIMARY KEY (`idusuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci AUTO_INCREMENT=1000;




-- Estructura de tabla para la tabla `propiedades`
--

CREATE TABLE `propiedades` (
  `idpropiedad` int(11) NOT NULL AUTO_INCREMENT,
  `estado` varchar(500) NOT NULL,
  `ciudad` varchar(500) NOT NULL,
  `colonia` varchar(500) DEFAULT NULL,
  `calle` varchar(500) DEFAULT NULL,
  `numero_exterior` varchar(50) DEFAULT NULL,
  `tipo_inmueble` varchar(70) NOT NULL,
  `transaccion` varchar(70) NOT NULL,
  `precio` decimal(38,0) NOT NULL,
  `codigo_proveedor` int(11) NOT NULL,
  `telefono_contacto` varchar(45) NOT NULL,
  `idusuario` int(11) NOT NULL,
  PRIMARY KEY (`idpropiedad`),
  KEY `idusuario` (`idusuario`),
  CONSTRAINT `propiedades_ibfk_1` FOREIGN KEY (`idusuario`) REFERENCES `usuarios` (`idusuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci AUTO_INCREMENT=5000;


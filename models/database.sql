CREATE DATABASE `trivial` /*!40100 DEFAULT CHARACTER SET utf8 */;


-- trivial.categorias definition

CREATE TABLE `categorias` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `categoria` varchar(100) NOT NULL,
  `notas` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8
COMMENT='Tabla de categorias para la clasificación de las preguntas';


-- trivial.subcategorias definition

CREATE TABLE `subcategorias` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `subcategoria` varchar(100) NOT NULL,
  `categoria_idx` int(11) NOT NULL,
  `notas` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `subcategorias_FK` (`categoria_idx`),
  CONSTRAINT `subcategorias_FK` FOREIGN KEY (`categoria_idx`) REFERENCES `categorias` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- trivial.niveles definition

CREATE TABLE `niveles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nivel` varchar(100) NOT NULL,
  `notas` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- trivial.tiempos definition

CREATE TABLE `tiempos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tiempo` varchar(100) NOT NULL,
  `notas` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- trivial.preguntas definition

CREATE TABLE `preguntas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pregunta` varchar(1024) NOT NULL,
  `respuesta_1` varchar(1024) NOT NULL,
  `respuesta_2` varchar(1024) NOT NULL,
  `respuesta_3` varchar(1024) NOT NULL,
  `respuesta_4` varchar(1024) NOT NULL,
  `respuesta_correcta` int(1) NOT NULL,
  `categoria_idx` int(11) NOT NULL,
  `subcategoria_idx` int(11) NOT NULL,
  `nivel_idx` int(11) NOT NULL,
  `tiempo_idx` int(11) NOT NULL,
  `notas` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_categorias` (`categoria_idx`),
  KEY `FK_subcategorias` (`subcategoria_idx`),
  KEY `FK_niveles` (`nivel_idx`),
  KEY `FK_tiempos` (`tiempo_idx`),
  CONSTRAINT `FK_categorias` FOREIGN KEY (`categoria_idx`) REFERENCES `categorias` (`id`),
  CONSTRAINT `FK_niveles` FOREIGN KEY (`nivel_idx`) REFERENCES `niveles` (`id`),
  CONSTRAINT `FK_subcategorias` FOREIGN KEY (`subcategoria_idx`) REFERENCES `subcategorias` (`id`),
  CONSTRAINT `FK_tiempos` FOREIGN KEY (`tiempo_idx`) REFERENCES `tiempos` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

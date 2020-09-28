-- DROP SCHEMA trivial_schema;

CREATE SCHEMA trivial_schema AUTHORIZATION trivial_user;

-- DROP TYPE trivial_schema."_categorias";

CREATE TYPE trivial_schema."_categorias" (
    INPUT = array_in,
    OUTPUT = array_out,
    RECEIVE = array_recv,
    SEND = array_send,
    ANALYZE = array_typanalyze,
    ALIGNMENT = 8,
    STORAGE = any,
    CATEGORY = A,
    ELEMENT = trivial_schema.categorias,
    DELIMITER = ',');

-- DROP TYPE trivial_schema."_niveles";

CREATE TYPE trivial_schema."_niveles" (
    INPUT = array_in,
    OUTPUT = array_out,
    RECEIVE = array_recv,
    SEND = array_send,
    ANALYZE = array_typanalyze,
    ALIGNMENT = 8,
    STORAGE = any,
    CATEGORY = A,
    ELEMENT = trivial_schema.niveles,
    DELIMITER = ',');

-- DROP TYPE trivial_schema."_preguntas";

CREATE TYPE trivial_schema."_preguntas" (
    INPUT = array_in,
    OUTPUT = array_out,
    RECEIVE = array_recv,
    SEND = array_send,
    ANALYZE = array_typanalyze,
    ALIGNMENT = 8,
    STORAGE = any,
    CATEGORY = A,
    ELEMENT = trivial_schema.preguntas,
    DELIMITER = ',');

-- DROP TYPE trivial_schema."_subcategorias";

CREATE TYPE trivial_schema."_subcategorias" (
    INPUT = array_in,
    OUTPUT = array_out,
    RECEIVE = array_recv,
    SEND = array_send,
    ANALYZE = array_typanalyze,
    ALIGNMENT = 8,
    STORAGE = any,
    CATEGORY = A,
    ELEMENT = trivial_schema.subcategorias,
    DELIMITER = ',');

-- DROP TYPE trivial_schema."_tiempos";

CREATE TYPE trivial_schema."_tiempos" (
    INPUT = array_in,
    OUTPUT = array_out,
    RECEIVE = array_recv,
    SEND = array_send,
    ANALYZE = array_typanalyze,
    ALIGNMENT = 8,
    STORAGE = any,
    CATEGORY = A,
    ELEMENT = trivial_schema.tiempos,
    DELIMITER = ',');

-- DROP SEQUENCE trivial_schema.categorias_id_seq;

CREATE SEQUENCE trivial_schema.categorias_id_seq
    INCREMENT BY 1
    MINVALUE 1
    MAXVALUE 2147483647
    START 1
    CACHE 1
    NO CYCLE;
-- DROP SEQUENCE trivial_schema.niveles_id_seq;

CREATE SEQUENCE trivial_schema.niveles_id_seq
    INCREMENT BY 1
    MINVALUE 1
    MAXVALUE 2147483647
    START 1
    CACHE 1
    NO CYCLE;
-- DROP SEQUENCE trivial_schema.preguntas_id_seq;

CREATE SEQUENCE trivial_schema.preguntas_id_seq
    INCREMENT BY 1
    MINVALUE 1
    MAXVALUE 2147483647
    START 1
    CACHE 1
    NO CYCLE;
-- DROP SEQUENCE trivial_schema.subcategorias_id_seq;

CREATE SEQUENCE trivial_schema.subcategorias_id_seq
    INCREMENT BY 1
    MINVALUE 1
    MAXVALUE 2147483647
    START 1
    CACHE 1
    NO CYCLE;
-- DROP SEQUENCE trivial_schema.tiempos_id_seq;

CREATE SEQUENCE trivial_schema.tiempos_id_seq
    INCREMENT BY 1
    MINVALUE 1
    MAXVALUE 2147483647
    START 1
    CACHE 1
    NO CYCLE;-- trivial_schema.categorias definition

-- Drop table

-- DROP TABLE trivial_schema.categorias;

CREATE TABLE trivial_schema.categorias (
    id serial NOT NULL,
    categoria varchar NOT NULL,
    notas varchar NULL,
    CONSTRAINT categorias_pk PRIMARY KEY (id)
);


-- trivial_schema.niveles definition

-- Drop table

-- DROP TABLE trivial_schema.niveles;

CREATE TABLE trivial_schema.niveles (
    id serial NOT NULL,
    nivel varchar NOT NULL,
    notas varchar NULL,
    CONSTRAINT niveles_pk PRIMARY KEY (id)
);


-- trivial_schema.tiempos definition

-- Drop table

-- DROP TABLE trivial_schema.tiempos;

CREATE TABLE trivial_schema.tiempos (
    id serial NOT NULL,
    tiempo varchar NOT NULL,
    notas varchar NULL,
    CONSTRAINT tiempos_pk PRIMARY KEY (id)
);


-- trivial_schema.subcategorias definition

-- Drop table

-- DROP TABLE trivial_schema.subcategorias;

CREATE TABLE trivial_schema.subcategorias (
    id serial NOT NULL,
    subcategoria varchar NOT NULL,
    id_categoria int4 NOT NULL,
    notas varchar NULL,
    CONSTRAINT subcategorias_pk PRIMARY KEY (id),
    CONSTRAINT categorias_fk FOREIGN KEY (id_categoria) REFERENCES trivial_schema.categorias(id)
);


-- trivial_schema.preguntas definition

-- Drop table

-- DROP TABLE trivial_schema.preguntas;

CREATE TABLE trivial_schema.preguntas (
    id serial NOT NULL,
    pregunta varchar NOT NULL,
    respuesta_1 varchar NOT NULL,
    respuesta_2 varchar NOT NULL,
    respuesta_3 varchar NOT NULL,
    respuesta_4 varchar NOT NULL,
    respuesta_correcta varchar NOT NULL,
    id_categoria int4 NOT NULL,
    id_subcategoria int4 NOT NULL,
    id_nivel int4 NOT NULL,
    id_tiempo int4 NOT NULL,
    notas varchar NULL,
    CONSTRAINT preguntas_pk PRIMARY KEY (id),
    CONSTRAINT categorias_fk FOREIGN KEY (id_categoria) REFERENCES trivial_schema.categorias(id),
    CONSTRAINT niveles_fk FOREIGN KEY (id_nivel) REFERENCES trivial_schema.niveles(id),
    CONSTRAINT subcategorias_fk FOREIGN KEY (id_subcategoria) REFERENCES trivial_schema.subcategorias(id),
    CONSTRAINT tiempos_fk FOREIGN KEY (id_tiempo) REFERENCES trivial_schema.tiempos(id)
);



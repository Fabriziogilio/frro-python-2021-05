"""Base de Datos SQL - Creación de tablas auxiliares"""

import sqlite3
from ejercicio_01 import borrar_tabla, crear_tabla


def crear_tabla_peso():
    """Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
        - IdPersona: Int() (Clave Foranea Persona)
        - Fecha: Date()
        - Peso: Int()
    """

    db = sqlite3.connect("base_datos.db")

    cursor = db.cursor()
    command = """CREATE TABLE IF NOT EXISTS PersonaPeso(
                idPersonaPeso INTEGER PRIMARY KEY AUTOINCREMENT,
                idPersona INTEGER,
                fecha DATETIME,
                peso INT,
                CONSTRAINT fk_Persona FOREIGN KEY (idPersona)
                REFERENCES Persona (idPersona))"""

    cursor.execute(command)
    db.commit()
    db.close()


def borrar_tabla_peso():
    """Implementar la funcion borrar_tabla, que borra la tabla creada
    anteriormente."""
    db = sqlite3.connect("base_datos.db")

    cursor = db.cursor()
    command = "DROP TABLE PersonaPeso"

    cursor.execute(command)
    db.commit()
    db.close()


# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN

"""Base de Datos SQL - Crear y Borrar Tablas"""

import sqlite3


def crear_tabla():
    """Implementar la funcion crear_tabla, que cree una tabla Persona con:
        - IdPersona: Int() (autoincremental)
        - Nombre: Char(30)
        - FechaNacimiento: Date()
        - DNI: Int()
        - Altura: Int()
    """

    db = sqlite3.connect("base_datos.db")

    cursor = db.cursor()
    command = """CREATE TABLE IF NOT EXISTS Persona(
                idPersona INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(30),
                fechaNacimiento DATETIME,
                dni INT,
                altura INT)"""

    cursor.execute(command)
    db.commit()
    db.close()


def borrar_tabla():
    """Implementar la funcion borrar_tabla, que borra la tabla creada
    anteriormente."""

    db = sqlite3.connect("base_datos.db")

    cursor = db.cursor()
    command = "DROP TABLE Persona"

    cursor.execute(command)
    db.commit()
    db.close()


# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN

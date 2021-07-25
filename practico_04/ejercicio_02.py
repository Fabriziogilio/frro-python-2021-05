"""Base de Datos SQL - Alta"""

import sqlite3
import datetime
from ejercicio_01 import reset_tabla


def agregar_persona(nombre, nacimiento, dni, altura):
    """Implementar la funcion agregar_persona, que inserte un registro en la
    tabla Persona y devuelva los datos ingresados el id del nuevo registro."""

    db = sqlite3.connect("base_datos.db")

    cursor = db.cursor()
    command = """INSERT INTO Persona (nombre, fechaNacimiento, dni, altura)
                values (?,?,?,?);"""

    cursor.execute(command, (nombre, nacimiento, dni, altura))
    db.commit()

    ultimo_id = cursor.lastrowid
    db.close()

    return ultimo_id


# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    id_marcela = agregar_persona('marcela gonzalez', datetime.datetime(1980, 1, 25), 12164492, 195)
    assert id_juan > 0
    assert id_marcela > id_juan


if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN

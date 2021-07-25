"""Base de Datos SQL - Búsqueda"""

import sqlite3
import datetime

from ejercicio_01 import reset_tabla
from ejercicio_02 import agregar_persona


def buscar_persona(id_persona):
    """Implementar la funcion buscar_persona, que devuelve el registro de una
    persona basado en su id. El return es una tupla que contiene sus campos:
    id, nombre, nacimiento, dni y altura. Si no encuentra ningun registro,
    devuelve False."""

    db = sqlite3.connect("base_datos.db")

    cursor = db.cursor()
    command = "SELECT * FROM Persona WHERE idPersona == ?"

    cursor.execute(command, [id_persona])
    persona = cursor.fetchone()

    db.close()

    if persona is not None:
        persona = list(persona)
        persona[2] = datetime.datetime.strptime(persona[2],
                                                "%Y-%m-%d %H:%M:%S")
        persona = tuple(persona)

        return persona
    return False


# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN

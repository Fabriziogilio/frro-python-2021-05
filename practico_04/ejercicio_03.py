"""Base de Datos SQL - Baja"""

import sqlite3
import datetime

from ejercicio_01 import reset_tabla
from ejercicio_02 import agregar_persona


def borrar_persona(id_persona):
    """Implementar la funcion borrar_persona, que elimina un registro en la
    tabla Persona. Devuelve un booleano en base a si encontro el registro y lo
    borro o no."""

    db = sqlite3.connect("base_datos.db")

    cursor = db.cursor()
    command = "DELETE FROM Persona WHERE idPersona == ?"

    cursor.execute(command, [id_persona])
    db.commit()
    rows = cursor.rowcount

    db.close()

    if rows > 0:
        return True
    return False

# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN

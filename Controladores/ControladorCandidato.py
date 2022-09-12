from Modelos.Candidato import Candidato


class ControladorCandidato():
    def __init__(self):
        print("Creando controlador candidato")
        self.

    # Funcion que trae la lista de todos los candidatos con sus atributos(READ)
    def index(self):
        print("Listando candidatos")
        unCandidato = {
            "_id": "abc123",
            "NoResolucion": "123",
            "cedula": "123",
            "nombre": "Pepito",
            "apellido": "Perez",
            "partido": "Politico"
        }
        return [unCandidato]

    # Funcion que crea un objeto de la clase candidato(CREATE)
    def create(self, infoCandidato):
        print("Creando candidato")
        elCandidato = Candidato(infoCandidato)
        return elCandidato.__dict__

    # Funcion para mostrar candidato especifico por ID(READ)
    def show(self, id):
        print("Mostrando candidato por su ID", id)
        elCandidato = {
            "_id": id,
            "NoResolucion": "123",
            "cedula": "123",
            "nombre": "Pepito",
            "apellido": "Perez",
            "partido": "Politico"
        }
        return elCandidato

    # Funcion para modificar informacion de un candidato(UPDATE)
    def update(self, id, infoCandidato):
        print("Actualizando candidato por su ID", id)
        elCandidato = Candidato(infoCandidato)
        return elCandidato.__dict__

    # Funcion de eliminacion de un candidato por su ID(DELETE)
    def delete(self, id):
        print("Eliminando candidato por su ID", id)
        return{"deleted_count": 1}
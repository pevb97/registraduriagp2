from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioPartido import RepositorioPartido

from Modelos.Candidato import Candidato
from Modelos.Partido import Partido


class ControladorCandidato():
    def __init__(self):
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioPartido = RepositorioPartido()

    # Funcion que trae la lista de todos los candidatos con sus atributos(READ)
    def index(self):
        return self.repositorioCandidato.findAll()

    # Funcion que crea un objeto de la clase candidato(CREATE)
    def create(self, infoCandidato):
        nuevoCandidato = Candidato(infoCandidato)
        return self.repositorioCandidato.save(nuevoCandidato)

    # Funcion para mostrar candidato especifico por ID(READ)
    def show(self, id):
        elCandidato = Candidato(self.repositorioCandidato.findById(id))
        return elCandidato.__dict__

    # Funcion para modificar informacion de un candidato(UPDATE)
    def update(self, id, infoCandidato):
        candidatoActual = Candidato(self.repositorioCandidato.findById(id))
        candidatoActual.nombre = infoCandidato["nombre"]
        candidatoActual.apellido = infoCandidato["apellido"]
        candidatoActual.cedula = infoCandidato["cedula"]
        candidatoActual.resolucion = infoCandidato["resolucion"]
        return self.repositorioCandidato.save(candidatoActual)

    # Funcion de eliminacion de un candidato por su ID(DELETE)
    def delete(self, id):
        return self.repositorioCandidato.delete(id)


    # Relacion entre Partido y Candidato (1 -> N)

    def asignarPartido(self, id, id_partido):
        candidatoActual = Candidato(self.repositorioCandidato.findById(id))
        partidoActual = Partido(self.repositorioPartido.findById(id_partido))
        candidatoActual.partido = partidoActual
        return self.repositorioCandidato.save(candidatoActual)
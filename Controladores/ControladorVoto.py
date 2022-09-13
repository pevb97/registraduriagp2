from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioMesas import RepositorioMesas
from Repositorios.RepositorioVoto import RepositorioVoto
from Modelos.Voto import Voto
from Modelos.Candidato import Candidato
from Modelos.Mesas import Mesas

class ControladorVoto():

    def __init__(self):
        self.repositorioVoto = RepositorioVoto()
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioMesa = RepositorioMesas()

    def index(self):
        return self.repositorioVoto.findAll()

    def create(self,infoVoto):
        nuevoVoto=Voto(infoVoto)
        return self.repositorioVoto.save(nuevoVoto)
    def show(self,id):
        elVoto=Voto(self.repositorioVoto.findById(id))
        return elVoto.__dict__
    def update(self,id,infoVoto):
        votoActual=Voto(self.repositorioVoto.findById(id))
        votoActual.fecha = infoVoto["fecha"]
        return self.repositorioVoto.save(votoActual)
    def delete(self,id):
        return self.repositorioVoto.delete(id)

    """ Dependencia Voto , candidato y mesa (N:N:N) """

    def asignarVoto(self, id, id_candidato, id_mesa):
        votoActual=Voto(self.repositorioVoto.findById(id))
        candidatoActual = Candidato(self.repositorioCandidato.findById(id_candidato))
        mesaActual = Mesas(self.repositorioMesa.findById(id_mesa))
        votoActual.candidato = candidatoActual
        votoActual.mesa = mesaActual
        return self.repositorioVoto.save(votoActual)
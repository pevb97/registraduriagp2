from Repositorios.RepositorioResolucion import RepositorioResolucion
from Repositorios.RepositorioPartido import RepositorioPartido
from Modelos.Resolucion import Resolucion
from Modelos.Partido import Partido

class ControladorResolucion():

    def __init__(self):
        self.repositorioResolucion = RepositorioResolucion()
        self.repositorioPartido = RepositorioPartido()

    def index(self):
        return self.repositorioResolucion.findAll()

    def create(self,infoResolucion):
        nuevoResolucion=Resolucion(infoResolucion)
        return self.repositorioResolucion.save(nuevoResolucion)
    def show(self,id):
        laResolucion=Resolucion(self.repositorioResolucion.findById(id))
        return laResolucion.__dict__
    def update(self,id,infoResolucion):
        ResolucionActual=Resolucion(self.repositorioResolucion.findById(id))
        ResolucionActual.fecha = infoResolucion["fecha"]
        return self.repositorioResolucion.save(ResolucionActual)
    def delete(self,id):
        return self.repositorioResolucion.delete(id)

    """ Dependencia Resolucion y Partido (1:1) """

    def asignarPartido(self, id, id_partido):
        ResolucionActual=Resolucion(self.repositorioResolucion.findById(id))
        PartidoActual = Partido(self.repositorioPartido.findById(id_partido))
        ResolucionActual.partido = PartidoActual
        return self.repositorioResolucion.save(ResolucionActual)
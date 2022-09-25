from Repositorios.RepositorioMesas import RepositorioMesas
from Modelos.Mesas import Mesas

class ControladorMesas():

    def __init__(self):
        self.repositorioMesas = RepositorioMesas()

    def index(self):
        return self.repositorioMesas.findAll()

    def create(self,infoMesas):
        nuevoMesas=Mesas(infoMesas)
        return self.repositorioMesas.save(nuevoMesas)
    def show(self,id):
        laMesa=Mesas(self.repositorioMesas.findById(id))
        return laMesa.__dict__
    def update(self,id,infoMesas):
        MesaActual=Mesas(self.repositorioMesas.findById(id))
        MesaActual.nombre = infoMesas["nombre"]
        MesaActual.descripcion = infoMesas["descripcion"]
        MesaActual.nrocedulas = infoMesas["nrocedulas"]
        return self.repositorioMesas.save(MesaActual)
    def delete(self,id):
        return self.repositorioMesas.delete(id)
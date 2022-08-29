from Modelos.Partido import Partido

class ControladorPartido():
    def __init__(self):
        print("Creando ControladorPartido")

    #Función que trae la lista de todos los partidos con sus atributos
    def index(self):
        print ("Listar todos los partidos")
        unPartido={
            "_id":"ColombiaHumana2022",
            "Nit":"12345",
            "Presidente":"Gustavo Petro",
            "movimiento":"izquierda"

        }
        return [unPartido]

    #Crear un objeto de la clase Partido y despues se manda a guardar con un metodo a la DB
    def create(self,infoPartido):
        print("Crear un partido")
        elPartido=Partido(infoPartido)
        return elPartido.__dict__


    #Funcion para mostrar un objeto Partido según su id
    def show(self,id):
        print("Mostrando un Partido con id", id)
        elPartido = {
            "_id":"ColombiaHumana2022",
            "Nit":"12345",
            "Presidente":"Gustavo Petro",
            "movimiento":"izquierda"
        }
        return elPartido

    # Funcion para actulizar la informacion de un Partido
    def update(self, id, infoPartido):
        print("Actualizando Partido con el id ", id)
        elPartido=Partido(infoPartido)
        return elPartido.__dict__

   # Funcion para eliminar un Partido
    def delete(self, id):
        print("Eliminando partido con el id ", id)
        return {"deletd_cout":1}
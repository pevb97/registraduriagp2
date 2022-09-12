from Modelos.Resultados import Resultados
from Repositorios.RepositorioResultados import RepositorioResultados


class ControladorResultados():
    def __init__(self):
        #print("Creando ControladorResultados")
        self.repositorioResultados = RepositorioResultados()


# Funcion que trae la lista de todos los resultados
    def index(self):
        """print("Listar a todos los resultados")
        unResultado={
            "Resultado 1": {
                "_idMesa": "17",
                "Candidato": "Andrés Rodriguez",
                "Partido": "Partido A",
                "Votos": "15"
            },

            "Resultado 2": {
                "_idMesa": "17",
                "Candidato": "Oscar Castaño",
                "Partido": "Partido A",
                "Votos": "5"
            },

            "Resultado 3": {
                "_idMesa": "23",
                "Candidato": "Patricia Olaya",
                "Partido": "Partido J",
                "Votos": "150"
            },

            'Resultado 4': {
                "_idMesa": "51",
                "Candidato": "Patricia Olaya",
                "Partido": "Partido J",
                "Votos": "37"
            },

            "Resultado 5": {
                "_idMesa": "6",
                "Candidato": "Omaira Arevalo",
                "Partido": "Partido A",
                "Votos": "56"
            },

            "Resultado 6": {
                "_idMesa": "187",
                "Candidato": "Paula Orozco",
                "Partido": "Partido M",
                "Votos": "1"
            },

            "Resultado 7": {
                "_idMesa": "1",
                "Candidato": "Antonio Patiño",
                "Partido": "Partido E",
                "Votos": "478"
            }
        }"""
        return self.repositorioResultados.findAll()

# Funcion para crear un resultado
    def create(self,infoResultados):
        #print("Crear un resultado")
        nuevoResultado = Resultados(infoResultados)
        return self.repositorioResultados.save(nuevoResultado)

# Funcion para mostrar un resultado segun su identificador
    def show(self,idResultado):
        #print("Mostrando un resultado con su id ", idResultado)
        elResultado = Resultados(self.repositorioResultados.findById(idResultado))
        return elResultado.__dict__

# Funcion para actualizar la información de un resultado
    def update(self,idResultado,infoResultados):
        #print("Actualizando resultado con el id ", idResultado)
        resultadoActual = Resultados(self.repositorioResultados.findById(idResultado))
        resultadoActual.Mesa = infoResultados["Mesa"]
        resultadoActual.Partido = infoResultados["Partido"]
        resultadoActual.Candidato = infoResultados["Candidato"]
        resultadoActual.Votos = infoResultados["Votos"]
        return self.repositorioResultados.save(resultadoActual)

# Funcion para eliminar un resultado
    def delete(self,idResultado):
        #print("Eliminando resultado con el id ", idResultado)
        return self.repositorioResultados.delete(idResultado)
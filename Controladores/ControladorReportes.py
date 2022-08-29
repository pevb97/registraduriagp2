from Modelos.Reportes import Reportes
class ControladorReportes():

    def __init__(self):
        print("Creando ControladorReportes")

    # Funcion que trae la lista de TODOS los candidatos
    def listadoCandidatos(self):
        print("Lista de todos los candidatos")
        listaCandidatos = {
            'Candidato 1':{
            "_idCandidato": "1",
            "cedula": "1111",
            "nombre": "Andrés",
            "apellido": "Rodriguez"
            },
            'Candidato 2': {
                "_idCandidato": "2",
                "cedula": "2222",
                "nombre": "Patricia",
                "apellido": "Olaya"
            },
            'Candidato 3': {
                "_idCandidato": "3",
                "cedula": "3333",
                "nombre": "Omaira",
                "apellido": "Arevalo"
            }
        }
        return [listaCandidatos]

    # Funcion para mostrar TODOS los candidatos segun la mesa
    def listadoCandidatoMesa(self, idMesa):
        print("Mostrando un estudiante con su id ", idMesa)
        listaMesa={
            "Candidato 1": {
                "Candidato": "Andrés Rodriguez",
                "Partido": "Partido A",
                "Votos": "15"
            },

            "Candidato 2": {
                "Candidato": "Oscar Castaño",
                "Partido": "Partido A",
                "Votos": "5"
            },

            "Candidato 3": {
                "Candidato": "Patricia Olaya",
                "Partido": "Partido J",
                "Votos": "150"
            }

        }
        return [listaMesa]

    # Funcion que trae la lista de TODAS las mesas
    def listadoMesas(self):
        print("Lista de todas las mesas con la participacion cuidadana ordenadas de menor a mayor")
        listaMesa = {
            'Mesa 302': "2",
            'Mesa 86': "7",
            'Mesa 3': "28",
            'Mesa 4': "58",
            'Mesa 145': "73",
            'Mesa 40': "94",
            'Mesa 27': "187",
            'Mesa 5': "194",
            'Mesa 54': "223"
        }
        return [listaMesa]

    # Funcion que muestra la lista de TODOS los partidos
    def listadoPartidos(self):
        print("Lista de todos los partidos ")
        listaPartido = {
            'Partido A': "47023",
            'Partido K': "33304",
            'Partido Z': "13100",
            'Partido R': "9852",
            'Partido T': "6788",
            'Partido Y': "4758",
            'Partido J': "1028",
            'Partido E': "587",
            'Partido M': "492"
        }
        return [listaPartido]

    # Funcion que muestra la lista de TODOS los partidos segun la mesa
    def listadoPartidosMesa(self,idMesa):
        print("Lista de todos los candidatos del partido seleccionado ", idMesa)
        listaPartidoMesa ={
            'Partido A': "7023",
            'Partido E': "6587",
            'Partido J': "1358",
            'Partido M': "492",
        }
        return [listaPartidoMesa]



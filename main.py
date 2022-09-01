from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

app = Flask(__name__)
cors = CORS(app)

from Controladores.ControladorUsuario import ControladorUsuario
miControladorUsuario=ControladorUsuario()

from Controladores.ControladorRoles import ControladorRoles
miControladorRoles=ControladorRoles()

from Controladores.ControladorPartido import ControladorPartido
miControladorPartido=ControladorPartido()

from Controladores.ControladorCandidato import ControladorCandidato
miControladorCandidato = ControladorCandidato()

from Controladores.ControladorReportes import ControladorReportes
miControladorReportes = ControladorReportes()

from Controladores.ControladorResultados import ControladorResultados
miControladorResultados = ControladorResultados()

## funcionalidad de prueba
@app.route("/", methods=['GET'])

def test():
    json = {}
    json["message"] = "Server running ..."
    return jsonify(json)

#usuarios

@app.route("/Usuarios",methods=['GET'])
def getUsuario():
    json=miControladorUsuario.index()
    return jsonify(json)


@app.route("/Usuarios",methods=['POST'])
def crearUsuario():
    data = request.get_json()
    json=miControladorUsuario.create(data)
    return jsonify(json)
@app.route("/Usuarios/<string:id>",methods=['GET'])
def getUsuario1(id):
    json=miControladorUsuario.show(id)
    return jsonify(json)
@app.route("/Usuarios/<string:id>",methods=['PUT'])
def modificarUsuario(id):
    data = request.get_json()
    json=miControladorUsuario.update(id,data)
    return jsonify(json)
@app.route("/Usuarios/<string:id>",methods=['DELETE'])
def eliminarUsuario(id):
    json=miControladorUsuario.delete(id)
    return jsonify(json)

#roles

@app.route("/Roles",methods=['GET'])
def getRol():
    json=miControladorRoles.index()
    return jsonify(json)
@app.route("/Roles/<string:id>",methods=['PUT'])
def modificarRol(id):
    data = request.get_json()
    json=miControladorRoles.update(id,data)
    return jsonify(json)

# candidatos



@app.route("/candidatos", methods=['GET'])

def getCandidatos():

    json = miControladorCandidato.index()

    return jsonify(json)

@app.route("/candidatos", methods=['POST'])

def crearCandidato():

    data = request.get_json()

    json = miControladorCandidato.create(data)

    return jsonify(json)

@app.route("/candidatos/<string:id>", methods=['GET'])

def getCandidato(id):

    json = miControladorCandidato.show(id)

    return jsonify(json)

@app.route("/candidatos/<string:id>", methods=['PUT'])

def modificarCandidato(id):

    data = request.get_json()

    json = miControladorCandidato.update(id, data)

    return jsonify(json)

@app.route("/candidatos/<string:id>", methods=['DELETE'])

def eliminarCandidato(id):

    json = miControladorCandidato.delete(id)

    return jsonify(json)

#partidos





@app.route("/partidos",methods=['GET'])

def getPartidos():

    json=miControladorPartido.index()

    return jsonify(json)

@app.route("/partidos",methods=['POST'])

def crearPartido():

    data = request.get_json()

    json=miControladorPartido.create(data)

    return jsonify(json)

@app.route("/partidos/<string:id>",methods=['GET'])

def getPartido(id):

    json=miControladorPartido.show(id)

    return jsonify(json)

@app.route("/partidos/<string:id>",methods=['PUT'])

def modificarPartido(id):

    data = request.get_json()

    json=miControladorPartido.update(id,data)

    return jsonify(json)

@app.route("/partidos/<string:id>",methods=['DELETE'])

def eliminarPartido(id):

    json=miControladorPartido.delete(id)

    return jsonify(json)

def loadFileConfig():

    with open('config.json') as file:

        data = json.load(file)

    return data



#resultados

# funcionalidad de obtener lista de los resultados
@app.route("/resultados",methods=['GET'])
def getAllResultados():
    json=miControladorResultados.index()
    return jsonify(json)

# funcionalidad de crear un resultado
@app.route("/resultados",methods=['POST'])
def crearResultados():
    data = request.get_json()
    json = miControladorResultados.create(data)
    return jsonify(json)

# funcionalidad de mostrar un resultado
@app.route("/resultados/<string:idResultado>",methods=['GET'])
def getResultadosId(idResultado):
    json=miControladorResultados.show(idResultado)
    return jsonify(json)

# funcionalidad de actualizar un resultado
@app.route("/resultados/<string:idResultado>",methods=['PUT'])
def modificarResultados(idResultado):
    data = request.get_json()
    json=miControladorResultados.update(idResultado,data)
    return jsonify(json)

# funcionalidad de eliminar un resultado
@app.route("/resultados/<string:idResultado>",methods=['DELETE'])
def eliminarResultados(idResultado):
    json=miControladorResultados.delete(idResultado)
    return jsonify(json)

#reportes

# Funcion que trae la lista de TODOS los candidatos
@app.route("/reportes/candidatos",methods=['GET'])
def getAllCandidatos():
    json=miControladorReportes.listadoCandidatos()
    return jsonify(json)

# Funcionalidad para mostrar TODOS los candidatos segun la mesa
@app.route("/reportes/candidatos/<string:idMesa>",methods=['GET'])
def getCandidatosIdMesa(idMesa):
    json=miControladorReportes.listadoCandidatoMesa(idMesa)
    return jsonify(json)

# Funcionalidad que trae la lista de TODAS las mesas
@app.route("/reportes/mesas",methods=['GET'])
def getAllMesas():
    json=miControladorReportes.listadoMesas()
    return jsonify(json)

# Funcionalidad que muestra la lista de TODOS los partidos
@app.route("/reportes/partidos",methods=['GET'])
def getAllPartidos():
    json=miControladorReportes.listadoPartidos()
    return jsonify(json)

# Funcionalidad que muestra la lista de TODOS los partidos segun la mesa
@app.route("/reportes/partidos/<string:idMesa>",methods=['GET'])
def getPartidosIdMesa(idMesa):
    json=miControladorReportes.listadoPartidosMesa(idMesa)
    return jsonify(json)


def loadFileConfig():
    with open('Config.json') as file:
        data = json.load(file)
    return data

if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])

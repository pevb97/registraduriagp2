from Modelos.Usuario import Usuario

class ControladorUsuario():
    def __init__(self):
        print("Creando ControladorUsuario")

    def index(self):
        print("Listando todos los usuarios")
        Usuario1= {
            "id": "1001",
            "Nombre":"Santiago Ramirez",
            "Correo":"elcorreo1@g2.com",
            "Contrasena":"elcorreo1@g2.com"
        }
        return [Usuario1]

    def create(self, infoUsuario):
        print("Crear un Usuario")
        Usuario2 = Usuario(infoUsuario)
        return Usuario2.__dict__

    def show(self, id):
        print("Mostrando un usuario con id ",id)

        Usuario3 = {
            "id": "1003",
            "Nombre": "Felipe Ramirez",
            "Correo": "elcorreo3@g2.com",
            "Contrasena": "elcorreo3@g2.com"
        }
        return [Usuario3]




    def update(self,id,infoUsuario):
         print("Actualizando usuario con id ",id)
         Usuario2 = Usuario(infoUsuario)
         return Usuario2.__dict__

    def delete(self,id):
        print("Elimiando usuario con id ",id)
        return {"deleted_count": 1}
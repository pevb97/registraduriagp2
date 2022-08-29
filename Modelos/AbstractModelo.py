from abc import ABCMeta

#Constructor

class AbstractModelo(metaclass=ABCMeta):
    def __init__(self, data):
        for llave, valor in data.items():
            setattr(self, llave, valor)
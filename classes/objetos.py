from classes import objeto


class Objetos:
    def __init__(self):
        self.objetos = []

    def addObjeto(self, nome, volume, valor):
        obj = objeto.Objeto(nome, volume, valor)
        self.objetos.append(obj)

    def add(self, objeto):
        self.objetos.append(objeto)

    def print(self):
        for item in self.objetos:
            print(item)

from classes import objeto


class Objetos:
    def __init__(self):
        self.objetos = []

    def addObjeto(self, nome, volume, valor):
        obj = objeto.Objeto(nome, volume, valor)
        print(obj)
        self.objetos.append(obj)
        print(self)
        for item in self.objetos:
            print(item)

    def print(self):
        print(self)
        for item in self.objetos:
            print(item)

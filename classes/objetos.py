from classes import objeto

class Objetos:
  def __init__ (self):
    self.objetos = {}

  def addObjeto (self, nome, volume, valor):
    objeto = objeto.Objeto(nome, volume, valor)
    self.objetos.append(objeto)

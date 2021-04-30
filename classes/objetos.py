from classes import objeto

class Objetos:
  def __init__ (self):
    self.objetos = []
    self.quantidade = 0

  def addObjeto (self, nome, volume, valor):
    objetoLocal = objeto.Objeto(nome, volume, valor)
    self.objetos.append(objetoLocal)
    self.quantidade = (self.quantidade) +  1

  def quantidade (self):
    qtd = self.quantidade
    print (str(qtd))

  def printar (self):
    for n in self.objetos:
      print(n)
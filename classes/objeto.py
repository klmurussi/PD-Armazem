class Objeto:
  def __init__ (self, nome, volume, valor):
    self.nome = nome
    self.volume = volume
    self.valor = valor

    def __repr__(self): 
      mensagem = "nome:%s volume:%s valor:%s" % (self.nome, self.volume, self.valor)
      return mensagem
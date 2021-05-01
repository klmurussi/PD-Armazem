class Objeto:
    def __init__(self, nome, volume, valor):
        self.nome = nome
        self.volume = volume
        self.valor = valor

    def __repr__(self):
        return repr("nome: " + self.nome + " Volume: " + str(self.volume) + " Valor: " + str(self.valor))

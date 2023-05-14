#Classe = modelo de representação de um objeto
#Objeto = objeto de fato, algo

class JogadorLoteria:
    def __init__(self,nome):
        self.nome = nome
        self.numeros = (12,12,11,5,73,2)

    def total(self):
        return sum(self.numeros)
    
jogador_1 = JogadorLoteria('ricardo')
jogador_2 = JogadorLoteria('richalison')

print(jogador_1.nome)
print(jogador_1.numeros)
print(jogador_1.total())

print(jogador_2.nome)
print(jogador_2.numeros)
print(jogador_2.total())

print(jogador_1==jogador_2)
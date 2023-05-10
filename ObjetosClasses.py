#Classe = modelo de representação de um objeto
#Objeto = objeto de fato, algo

class JogadorLoteria:
    def __init__(self):
        self.nome = 'Pedro'
        self.numeros = (12,12,11,5,73,2)

    def total(self):
        return sum(self.numeros)
    
jogador_1 = JogadorLoteria()
jogador_2 = JogadorLoteria()

print(jogador_1.nome)
print(jogador_1.numeros)
print(jogador_1.total())
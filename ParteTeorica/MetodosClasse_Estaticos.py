class Funcionario():
    
    aumento = 1.04
    
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        
    def dados(self):
        return{'nome': self.nome, 'salario': self.salario}
    
    def aplicar_aumento(self):
        self.salario = self.salario * self.aumento
    
    @classmethod
    def definir_novo_aumento(cls, novo_aumento):
        cls.aumento = novo_aumento
        
    @staticmethod
    def dia_util(dia):
        #segunda = 0, domingo = 6
        if dia.weekday() == 5 or dia.weekday == 6:
            return False
        return True
        
        
modric = Funcionario('Modric', 1000)

print(modric.dados())

#modric.aplicar_aumento()

print(modric.dados())

Funcionario.definir_novo_aumento(1.05)

modric.aplicar_aumento()

print(modric.dados())

dlc = Funcionario('Fudido', 200)

dlc.aplicar_aumento()

print(dlc.dados())

import datetime

minha_data = datetime.date(2023, 5, 5)

print(Funcionario.dia_util(minha_data))
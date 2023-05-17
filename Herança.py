class Funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        
    def dados(self):
        return{'nome': self.nome, 'salario': self.salario}
    
yas = Funcionario('Yasmin', 0)
    
print(yas.dados())

class Admin(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
        
    def atualizar_dados(self, nome, salario):
        self.nome = nome
        self.salario = salario
        return self.dados()

vesgo = Admin('Arthur', 5000)

print(yas.dados())
print(vesgo.dados())

vesgo.atualizar_dados('socorro', 0)

print(vesgo.dados())


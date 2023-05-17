dicionario = [{'nome':'Cafu', 'idade': '48'},
              {'nome':'Deliz', 'idade': '18'},
              {'nome':'Fia do Cafu', 'idade': 'foudase'}]

x = int(input('Insira um numero de 0 a 2: '))

dicionario[2]['idade'] = '12'

print(dicionario[x])

d = {}

for i in range (0,2):
    f = str(input("Nome do funcionario: "))
    ind = int(input("Indice do funcionario: "))
    d.update({ind: f})

print  ("Funcionarios cadastrados: ", d)

rmv = input("deseja demitir um funcionaio? (s) para e (n) para não: \n")

copia = dict(d)

if rmv == "s":
    cod = int(input("Qual o codigo do funcionario que deseja remover: \n"))
    d.pop(cod)
    print ("funcionario", copia.get(cod)) , "removido"

print ("os funcionarios que sobraram foi: ", d)
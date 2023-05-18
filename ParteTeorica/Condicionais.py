pessoas_conhecidas = ['bunda', 'modric', 'pobre', 'desempregado', 'chamine', 'doka']

pessoa = str(input("Insira uma pessoa: "))

if pessoa in pessoas_conhecidas:
    print("Você conhece {}".format(pessoa))
else:
    print("Você não conhece {}".format(pessoa))
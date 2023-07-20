# args = argumentos
#kwargs = keyword arguments (argumentos de palavras-chave)

def meu_metodo(arg1, arg2):
    return arg1 + arg2
print(meu_metodo(4,5))

def meu_metodo_longo(arg1,arg2,arg3,arg4):
    return arg1 + arg2 + arg3 + arg4
print(meu_metodo_longo(23,321,51,4))

def minha_lista_somada(lista):
    return sum(lista)

print(minha_lista_somada([3,3245,2,35,11,4,5,]))

def soma_simplifcada(*args):
    return sum(args)

print(soma_simplifcada(23,12,4,5,5,2,))

def metodo_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)
    
metodo_kwargs(3, 'wefn', 23, 'cu', nome='ana',idade=25)

#args antes dos kwargs

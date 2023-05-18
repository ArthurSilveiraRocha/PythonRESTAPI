import functools

def meu_decorador(funcao):
    @functools.wraps(funcao)
    def func_que_roda_funcao():
        print('******emrulhando funcao no decorador*****')
        funcao()
        print('*****fechando embrulho******')
    return func_que_roda_funcao

@meu_decorador
def minha_funcao():
    print('eu sou uma funcao')
print(minha_funcao())
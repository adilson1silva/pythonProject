'''
1 - interactive help     -- help()
2 - docs string          -- abrir três aspas duplas ("""""")
3 - parametros opcionais --
4 - escopo de variaveis - escopo global e escopo local
5 - retornar valores -- return

'''
# ------------------------------------------------------------------------------
'''def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor 
    :return:
    Função criado por Adilson silva
    """
    s = a + b + c
    print(f'A soma dos valores é {s}')

somar(2, 3, 5)

# ------------------------------- escopo de variaveis  ------------------------------------------------
def função():
    n1 = 4
    print(f'N1 por dentro vale {n1}')

n1 = 2
função()
print(f'N1 por fora vale {n1}')

#------------------------------------------ restornar valores --------------------------------
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(3, 5, 6)
r2 = somar(4, 5)
r3 = somar(6)
print(f'Os resoltados foram {r1}, {r2} e {r3}')

#----------------------------- parte pratica -------------------------------------------------
#----------------------------- parte pratica -------------------------------------------------

def fatorail(num=1):
    f = 1
    for c in range(num, 1, -1):
        f *= c
    return f

r1 = fatorail(3)
r2 = fatorail(5)
r3 = fatorail(7)
print(f'O fatorial dos números é igual a {r1}, {r2} e {r3}')

#-------------------------------------------- retornar booliano -------------------

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
num = int(input('digite um número: '))
if par(num):
    print('Par')
else:
    print('Impar')

#--------------------------------------------------------------------------------------

def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

#inicio de programa
a = 5
teste(a)
print(f'A fora vale {a}')


'''

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


#programa principal
#n = int(input('Digite um número: '))
f1 = fatorial(5)
f2 = fatorial(2)
f3 = fatorial(4)
print(f'Os resultados são {f1}, {f2} e {f3}')




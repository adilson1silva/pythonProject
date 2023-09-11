"""
def lin():
    print('-'*30)


#programa principal
lin()
print('Curso em vídeo')
lin()
print('Adilsn Silva')
lin()
print('Esforça para ser melhor do que ontem')
lin()
"""

#--------------------------------------------------------------------
"""
def titulo(txt):
    print('-'*30)
    print(txt)
    print('-'*30)


#programa principal
titulo('Curso em vídeo')
titulo('Adilson Silva')
titulo('Gustavo Guanabara')
titulo('Aprendendo python')
"""

#-----------------------------------------------------------------

"""
def soma(a, b):
    s = a + b
    print(f'A soma de {a} + {b} = {s}')


#programa principal
soma(4, 5)
soma(8, 9)
soma(2, 1)
soma(b=6, a=5)
"""

#--------------------------------------------------------------------
"""
def contador(*num):
    for n in num:
        print(n, end=' ')
    print('fim')
    tam = len(num)
    print(f'no total de {tam} números')

#programa principal
contador(1, 2, 5)
contador(5, 8, 9, 6)
contador(2, 6, 4, 3, 8, 10, 25)

"""

#--------------------------------------------------------------------------
"""
def dobrar(num):
    pos = 0
    while pos < len(num):
        num[pos] *= 2
        pos += 1


# Programa principal
lista = [1, 3, 5, 7, 9]
dobrar(lista)
print(lista)

lista_1 = [2, 4, 6, 7, 9, 3]
dobrar(lista_1)
print(lista_1)
"""


#----------------------------------------------------------------------------------------
def soma(*num):
    s = 0
    for n in num:
        s += n
    print(f'O valor da soma dos valores é de {s}')


soma(1, 3, 4, 5, 6)
soma(0, 2, 6)



'''
Modularização

foco:
- Dividir um programa grande
- Aumentar a legibilidade
- Facilitar a manutenção
'''

'''
# teórico
from uteis import numeros



num = int(input('Digite um numero: '))
fact = numeros.fatorial(num)
print(f'\033[0;33mO fatorial do número {num} é {fact}\033[m')
print(f'\033[0;34mO dobro do número {num} é {numeros.dobro(num)}\033[m')
print(f'\033[0;35mO triplo do número {num} é {numeros.triplo(num)}\033[m')
'''
'''
Pacotes

Nada mais nada menos de que varios modulos divididos por assunto 
exemplo
pacotes para manipulação de string 
pacotes para manipulação de datas
pacotes para manipulação de números 
pacotes para manipulação de cores
'''

def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f

def dobro(n):
    d = n * 2
    return d

def triplo(n):
    t = n * 3
    return t

#programa principal
num = int(input('Digite um número: '))
fat = fatorial(num)
do = dobro(num)
tri = triplo(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {do}')
print(f'O triplo de {num} é {tri}')
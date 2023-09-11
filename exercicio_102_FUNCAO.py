'''
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o
primeiro que indique o número a calcular e outro chamado show, que será um valor
lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo
do fatorial.
'''

def fatorial():
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return (f)


#programa principal
num = int(input('Digite um número: '))
print(f'O fatorial de {num} é {fatorial()}')
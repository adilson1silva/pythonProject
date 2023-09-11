"""
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros
com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual
deles é o maior.
"""
from time import sleep
def maior(*num):
    print('=-'*30)
    print('Analizando os valores...')
    sleep(0.5)
    maior = count = 0
    for n in num:
        if count == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        count += 1
    print(f'O maior valor digitado é {maior}')


#programa principal
maior(2, 5, 4, 9, 6)
maior(2, 56, 91, 6, 4)
maior()

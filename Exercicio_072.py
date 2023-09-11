'''
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por
extenso, de zero até vinte.

Seu programa deverá ler um número pelo teclado (entre 0 - 20) e mostrá-lo por extenso.
'''

'''
cont = 'zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',\
    'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito',\
    'dezenove', 'vinte'

num = int(input('Digite um numero entre 0 e 20: '))
while True:
    if num > 20 or num < 0:
        num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    else:
        break

print(f'\033[1;34m Você escreveu {cont[num]}')

#...............................................................................

numeros = 'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',\
          'Dez', 'onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'dezesseis', 'dezessete', 'dezoito', 'desenove', 'vinte'
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num > 20 or num < 0:
        print('Tente novamente! Digite um número entre 0 e 20: ')
    else:
        break
print(f'Você digitou o número {numeros[num]}')

'''

numeros = 'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',\
          'Dez', 'onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'dezesseis', 'dezessete', 'dezoito', 'desenove', 'vinte'

while True:
    num = int(input('Digite um número [0, 20]: '))
    if num >= 0 and num <= 20:
        break
print(numeros[num])
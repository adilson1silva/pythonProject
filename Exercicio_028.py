'''
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

from random import randint
from time import sleep
computador = randint(0,5)
print('=-' * 30)
print('\033[0;34mpense num número entre 0 a 5\033[0;0m')
print('=-' * 30)
num = int(input('Didite um número [0, 5]: '))
print('pensando...')
sleep(2)
print(f'O computador jogou {computador}')
if num == computador:
    print('\033[0;34mVocê venceu!\033[0;0m')
else:
    print('\033[0;35mVocê perdeu!\033[0;0m')

'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o
menor e o maior valor que estão na tupla.
'''

from random import randint
num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os números sortiados são:')
for c in num:
    print(c, end=' , ')
print(f'\nO maior valor sortiado foi o {max(num)}')
print(f'O menor valor sortiado foi o {min(num)}')
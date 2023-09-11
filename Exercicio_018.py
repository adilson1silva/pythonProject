'''
Faça um programa que leia um ângulo qualquer o mostre na tela o valor do seno,
coseno e tangente desse ângulo
'''


import math
angulo = float(input('Digite um angulo: '))
print('Os resultados estão aqui em baixo: ')
print(f'O seno do angulo de {angulo}º é igual a {math.sin(math.radians(angulo)):1f}')
print(f'O coseno do angulo de {angulo}º é igual a {math.cos(math.radians(angulo)):1f}')
print(f'A tangente do angulo {angulo}º é igual a {math.tan(math.radians(angulo)):1f}')
print('Fim! Volte sempre!')



"""


angulo = float(input('Digite um ângulo: '))
print(f'O seno do ângulo {angulo} é igual a {math.sin(math.radians(angulo)):.2f}')
print(f'O coseno do ângulo {angulo} é igual a {math.cos(math.radians(angulo)):.2f}')
print(f'O tangente do ângulo {angulo} é igual a {math.tan(math.radians(angulo)):.2f}')
"""
import math

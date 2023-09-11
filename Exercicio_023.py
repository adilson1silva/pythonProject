'''
Faca um programa que leia um número de 0 a 999 e mostre na tela cada um dos
digitos separados
'''

num = int(input('Digite um numero [0 999]: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('----------- Analizando dados ------------')
print(f'Unidade {u}')
print(f'Dezena {d}')
print(f'Centena {c}')
print(f'Milhar {m}')
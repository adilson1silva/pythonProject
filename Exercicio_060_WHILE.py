'''
Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
'''

num = int(input('Digite um número: '))
count = num
res = 1
print(f'Calculando {num}! = ',end='')
while count > 0:
    print(f'{count}',end='')
    res *= count
    print(' x ' if count > 1 else ' = ',end='')
    count -= 1
print(res)
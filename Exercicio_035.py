'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se
elas podem ou não formar um triângulo.
'''

print('=-' * 30)
a = 'Analizar triângulos'
print(f'{a.center(50)}')
print('=-'*30)

seg1 = float(input('segmento 1: '))
seg2 = float(input('Segmento 2: '))
seg3 = float(input('segmento 3: '))

if seg3 < seg2 + seg1 and seg2 < seg3 + seg1 and seg1 < seg3 + seg2:
    print('forma um triângulo')
else:
    print('Não forma um triângulo')
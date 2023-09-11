'''
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço
da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens
mais longas.
'''

dist = int(input('Qual a distância da tua viagem? [Km] '))
if dist <= 200:
    print(f'O preço da tua viagem é de R${dist * 0.50:.2f}')
else:
    print(f'O preço da tua viagem é de R${dist * 0.45:.2f}')
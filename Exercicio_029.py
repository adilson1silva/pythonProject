'''
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada
Km acima do limite.
'''

vel = int(input('Digite a velocidade do veicúlo [Km/h]: '))
if vel <= 80:
    print('\033[0;32mTenha um bom dia! Dirija com segurança!\033[0;0m')
else:
    print(f'\033[0;31mMultado! Você excedeu o limite permitido que é 80 Km/h\033[0;0m\n'
          f'\033[0;31mVocê deve pagar uma multa de R${(vel - 80) * 7:.2f}\n\033[0;0m'
          f'\033[0;33mTenha um bom dia! dirija com segurança\033[0;0m')



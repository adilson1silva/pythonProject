'''
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o
programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''
conut50 = coun20 = count10 = count1 = 0
val = int(input('Qual o vaor a ser sacado: '))
while True:
    if val >= 50:
        val = val - 50
        conut50 += 1
    elif val >= 20:
        val = val - 20
        coun20 += 1
    elif val >= 10:
        val = val - 10
        count10 += 1
    elif val >= 1:
        val = val - 1
        count1 += 1
    if val <= 0:
        break
print(f'Total de {conut50} celulas de R$50')
print(f'total de {coun20} celulas de R$20')
print(f'total de {count10} celulas de R$10')
print(f'total de {count1} celulas de R$1')

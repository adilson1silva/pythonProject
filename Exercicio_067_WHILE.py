'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada
valor digitado pelo usuário. O programa será interrompido quando o número solicitado
for negativo.
'''


num = 0
while True:
    num = int(input('Digite um valor para a sua tabuada: '))
    if num < 0:
        print('OBRIGADO E VOLTE SEMPRE!!!')
        break
    else:
        print(f'Tabuada de {num}')
        for c in range(1, 11):
            print(f'{num} x {c} = {num * c}')



"""
while True:
    num = int(input('Digine o número para a sua atbuada: '))
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{c} * {num}  = {c * num}')
    print('-='*30)
print('PROGRAMA DE TABUADO INCERADO. VOLTE SEMPRE!')
"""

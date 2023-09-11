'''
Crie um programa que leia números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a
condição de parada. No final, mostre quantos números foram digitados e
qual foi a soma entre elas (desconsiderando o flag).
'''


num = count = soma = 0
while num != 999:
    num = int(input('Digite um número: '))
    if num != 999:
        soma += num
        count += 1
print(f'Foram digitados {count} números')
print(f'A soma dos números foi de {soma}')




"""
count = soma = 0
while True:
    num = int(input('Digite um número (999 para parar): '))
    if num == 999:
        break
    count += 1
    soma += num
print(f'Foram digitados {count} números.')
print(f'A soma entre os números digitados foi {soma}')
"""

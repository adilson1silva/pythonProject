'''
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior
e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não
continuar a digitar valores.
'''


maior_val = menor_val = count = soma = médio = 0
perguntar = ' '
while perguntar != 'N':
    num = int(input('Digite um valor interiro: '))
    perguntar = str(input('Deseja continuar? [S/N]'))[0].strip().upper()
    while perguntar not in "SN":
        perguntar = str(input('Deseja continuar? digite [S/N]'))[0].strip().upper()
    soma += num
    count += 1
    if count == 1:
        maior_val = num
        menor_val = num
    else:
        if num > maior_val:
            maior_val = num
        if num < menor_val:
            menor_val = num
média = soma/count
print('Apresentar resultados')
print('=-'*13)
print(f'Foram digitados {count} números')
print(f'A soma dos falores digitadoe é {soma}')
print(f'A média dos valores digitados foi {média}')
print(f'O maior valor digitado foi {maior_val}')
print(f'O menos valor digitado foi {menor_val}')
print('VOLTE SEMPRE!!!')




"""
#num = int(input('Digite um número: '))
continuar = ' '
count = soma = maior_val = menor_val = 0
while continuar != "N":
    num = int(input('Digite um número: '))
    count += 1
    soma += num
    if count == 1:
        maior_val = menor_val = num
    else:
        if num > maior_val:
            maior_val = num
        if num < menor_val:
            menor_val = num
    continuar = str(input('Quer continuar [N/S]: ')).upper()
    while continuar not in "SN":
        continuar = str(input('Quer continuar [N/S]: ')).upper()
print(f'A média dos números digitados é de {soma/count}')
print(f'O maios valor digitado é {maior_val}')
print(f'O menor valor digitado é {menor_val}')
"""


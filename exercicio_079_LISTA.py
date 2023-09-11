'''
crie um programa onde o usuario passa digitar varios valores numericos ecadastra-os em
uma lista. caso o númera já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os volores únicos digitados, em ordem crescente
'''
'''
listanum = []
while True:
    continuar = ' '
    num = [int(input('digite um valor: '))]
    if num not in listanum:
        listanum.append(num)
        listanum.sort()
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado...Não vou adicionar')
    while continuar not in 'SsNn':
            continuar = str(input('Quer continuar [S/N): ')).strip().upper()
    if continuar in 'Nn':
        break
print('-='*30)
print(f'Você digitou os numeros {listanum}')
'''
#.................................... exercitar.....................................
listnum = []
while True:
    num = (int(input('Digite um valor: ')))
    if num not in listnum:
        listnum.append(num)
        listnum.sort()
    else:
        print('Valor duplicado. Não vou adicionar...')
    while True:
        continuar = str(input('Quer Continuar [S/N]: ')).upper()
        if continuar in "SN":
            break
    if continuar == "N":
        break
print('-='*30)
print(f'Você digitou os valores {listnum}')
















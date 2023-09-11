'''
Faça um programa que leia o peso de varias pessoas guardando tudo em uma lista. no final,
mostre:
a) quantos listas foram cadastradas
b) uma listagem com as pessoas mais pesadas
c) uma listagem com as pessoas mais leves
'''
'''
count = maior_p = meno_p = 0
l_principal = list()
pessoas = list()
while True:
    continuar = ' '
    pessoas.append(str(input('Nome: ')))
    pessoas.append(int(input('Peso: ')))
    count += 1
    if len(l_principal) == 0:
        maior_p = meno_p = pessoas[1]
    else:
        if pessoas[1] > maior_p:
            maior_p = pessoas[1]
        elif pessoas[1] < meno_p:
            meno_p = pessoas[1]
    l_principal.append(pessoas[:])
    pessoas.clear()
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar [S/N]? ')).strip().upper()
    if continuar in 'N':
        break
print(f'Ao todo, você cadastrou {count} pessoas.')
print(f'O maior peso foi de {maior_p}Kg. peso de ', end='')
for p in l_principal:
    if p[1] == maior_p:
        print(f'{p[0]}')
print(f'O menor peso foi de {meno_p}Kg. peso de ', end='')
for p in l_principal:
    if p[1] == meno_p:
        print(f'{p[0]}')
'''
#--------------------------- exercitanto ---------------------------

lisapessoas = []
dados = []
maior_peso = menor_peso = count = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(lisapessoas) == 0:
        maior_peso = menor_peso = dados[1]
    else:
        if dados[1] > maior_peso:
            maior_peso = dados[1]
        if dados[1] < menor_peso:
            menor_peso = dados[1]
    lisapessoas.append(dados[:])
    count += 1
    dados.clear()
    while True:
        continuar = str(input('Quer continuar [S/N]: ')).upper()
        if continuar in "NS":
            break
    if continuar == "N":
        break
print('---------------- RESULTADO -------------')
print(f'No total você cadastrou {count} pessoas. ')
#print(f'As pessoas cadastradas foram {lisapessoas}')
print(f'O maior peso foi { maior_peso} kg. peso de', end=' ')
for p in lisapessoas:
    if p[1] == maior_peso:
        print(f'[{p[0]}]',end=' ')
print()
print(f'\nO menor peso foi de {menor_peso} kg. Peso de', end=' ')
for p in lisapessoas:
    if p[1] == menor_peso:
        print(f'[{p[0]}]', end=' ')
print()












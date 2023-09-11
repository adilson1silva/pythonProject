'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados
de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média


dados = {}
dados_p = []
dados_p1 = []
count = s_idade = 0
mulher = []
a_media = []
while True:
    continuar = sexo = ' '
    nome = str(input('Nome: '))
    dados['nome'] = nome
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        dados['sexo'] = sexo
        if sexo in 'F':
            mulher.append(nome)
        if sexo not in 'MF':
            print('ERRO! Por favor, digite apenas M ou F')
    idade = int(input('Idade: '))
    count += 1
    s_idade += idade
    m_idade = s_idade/count
    dados['idade'] = idade
    dados_p.append(dados)
    dados_p1.append(dados_p[:])
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if continuar not in 'SN':
            print('ERRO! Rosponda apenas S ou N')
    if continuar == 'N':
        break
print(f' A) Ao todo temos {count} pessoas cadastradas.')
print(f' B) A média de idade é de {m_idade:5.2f} anos.')
print(f'C) As mulheres cadastradas foram {mulher}')
print(f'D) A lista de pessoas que estão acima da média: ')
if idade >= m_idade:
    a_media.append(dados)
    for k, v in enumerate(a_media):
        print(f'{k}  {v} = {v}',end=' ')

'''
#----------------------------- Exercitanto ----------------------
tot = soma_idade = 0
dados_mulher = []
dados_idade = []
dados_nome = []
dados_principal = {}
while True:
    nome = str(input('Nome: '))
    dados_nome.append(nome)
    tot += 1
    while True:
        sexo = str(input('Sexo: ')).strip().upper()
        if sexo not in "MF":
            print('Preenche o campo sexo com "M" ou "F"')
        if sexo == "F":
            dados_mulher.append(nome)
        if sexo in "MF":
            break
    idade = int(input('Idade: '))
    dados_idade.append(idade)
    soma_idade += idade
    while True:
        continuar = str(input('Quer continuar [S/N]')).strip().upper()
        if continuar != "N" and continuar != "S":
                print('preenche o campo novamente: ')
        if continuar in "SN":
            break
    dados_principal["nome"] = dados_nome[:]
    dados_principal["idade"] = dados_idade[:]
    if continuar == "N":
        break

media = soma_idade/tot
print(f'Ao todo temos {tot} pessoas cadastradas.')
print(f'A média das idades foi de {media}.')
print(f'As mulheres cadastradas foram {dados_mulher}.')
print(f'As pessoas com idade acida da média foram: ')
for c, e in enumerate(dados_idade):
    if e >= media:
        print(f'[{dados_principal["nome"][c]} = {dados_principal["idade"][c]}]',end=' ')






















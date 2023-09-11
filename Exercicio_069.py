'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
'''

count_i = continuar = count_h = count_m = 0
while True:
    idade = int(input("Digite a idade de uma pessoa: "))
    if idade >= 18:
        count_i += 1
    while True:
        sexo = str(input("Digite o sexo [M/F]: ")).strip().upper()
        if sexo in "MF":
            if sexo == "M":
                count_h += 1
            if sexo == "F":
                if idade <= 20:
                    count_m += 1
            break
    while True:
        continuar = str(input("Deseja continuar [S/N]: ")).strip().upper()
        if continuar != "SN":
            break
    if continuar == "N":
        break
print(f'Foram digitados {count_i} pessoas com mais de 18 anos.')
print(f'Foram registados {count_h} homens durante o processo.')
print(f'Foram digitados {count_m} mulheres com menos de 20 anos.')














'''

count_18 = count_homens = count_m = 0
while True:
    idade = int(input('Idade: '))
    while True:
        sexo = str(input('Sexo: ')).upper()
        if sexo in 'MF':
            break
    if idade >= 18:
        count_18 += 1
    if sexo == 'M':
        count_homens += 1
    if sexo == 'F':
        if idade <= 20:
            count_m += 1
    print('-'*15)
    while True:
        continuar = str(input('Quer continuar [S/N]: ')).upper()
        if continuar in "SN":
            break
    if continuar == 'N':
        break
print(f'Foram cadastrado {count_18} pessoas com mais de 18 anos.')
print(f'foram cadastrados {count_m} mulheres com menos de 20 anos.')
print(f'Foram cadastradas {count_homens} homens')

'''


'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
'''

média = 0
h_m_v = ''
m_m_20 = 0
soma = 0
count = 0
count_m = 0
for c in range(0, 4):
    nome = str(input('Digite o nome: '))
    sexo = str(input('Digite o sexo: ')).upper()
    idade = int(input('Digite a idade: '))
    soma += idade
    média = soma / 4
    count += 1
    if sexo == 'M':
        if count == 1:
            h_m_v = idade
        elif idade > h_m_v:
            h_m_v = idade
    else:
        if idade < 20:
            count_m += 1
print(f'A média da idade do grupo é de {média} anos')
print(f'O homem mais velho tem {h_m_v} anos')
print(f'{count_m} mulheres tem menos do que 20 anos.')
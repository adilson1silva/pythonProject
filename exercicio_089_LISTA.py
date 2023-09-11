'''
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma
lista composta. No final, mostre um boletim contendo a média de cada um e permita
que o usuário possa mostrar as notas de cada aluno individualmente.


lista = []
cont = ' '
while True:
    non = (str(input('Nome: '))).strip()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    cont = str(input('quer continuar [S/N]? ')).strip().upper()
    media = (nota1 + nota2)/2
    lista.append([non, [nota1, nota2], media])
    if cont in 'N':
        break
print('='*30)
print(f'{"nome":<5} {"média":>15}')
print('-'*30)
for i, l in enumerate(lista):
    print(f'{i}: {l[0]:<5} {l[2]:>10.2f}')
while True:
    print('-'*30)
    mostr = int(input('Mostrar a nota de qual aluno [999 interrompe]: '))
    if mostr == 999:
        print('finalizando...')
        break
    if mostr <= len(lista)-1:
        print(f'Notas do {lista[mostr][0]} são {lista[mostr][1]}')

'''


# ------------------------------- Exercitando ------------------------

lista = []
while True:
    nome = str(input('Nome: '))
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    media = (nota_1 + nota_2) / 2
    lista.append([nome, [nota_1, nota_2], media])
    while True:
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()
        if continuar in "SN":
            break
    if continuar == "N":
        break
print(f'{"No.":<5} {"Nome: ":<8} {"Média: ":>5}')
for i, l in enumerate(lista):
    print(f'{i:<5} {l[0]:<8} {l[2]:>5}')
while True:
    mostrar = int(input('Mostrar notas de qual aluno:[999 para terminar]  '))
    if mostrar <= len(lista):
        print(f'Notas de {lista[mostrar][0]} são: {lista[mostrar][1]}')
    else:
        print('Digite novamente')
    if mostrar == 999:
        print('Processando')
        break
print('Volte sempre!')
























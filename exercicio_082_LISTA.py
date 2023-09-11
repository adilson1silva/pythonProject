'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
crie duas listas extras que vão conter apenas os valores pares e os valores ímpares
digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
'''
'''
listnum = []
listpar = []
listimpa = []
while True:
    continuar = ' '
    num = int(input('Digite um número: '))
    listnum.append(num)
    if num % 2 == 0:
        listpar.append(num)
    elif num % 2 != 0:
        listimpa.append(num)
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar [S/N]: ')).strip().upper()
    if continuar in 'N':
        break
print(f'A lista completa é {listnum}')
print(f'A lista de pares é {listpar}')
print(f'A lista de impares é {listimpa}')
'''
#......................... Exercitar .................................
listnum = []
listpar = []
listimpar = []
while True:
    listnum.append(int(input('Digite um valor: ')))
    while True:
        continuar = str(input('Quer continuar [S/N]: ')).upper()
        if continuar in "NS":
            break
    if continuar == "N":
        break
print(f'A lista conpleta é {listnum}')
for c in range(0, len(listnum)):
    if listnum[c] % 2 == 0:
        listpar.append(listnum[c])
    if listnum[c] % 2 == 1:
        listimpar.append(listnum[c])
print(f'A lista de pares é {listpar}')
print(f'A lista de impares é {listimpar}')











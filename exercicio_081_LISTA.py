'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''
'''
count = 0
listval = []
while True:
    continuar = ' '
    val = int(input('digite um valor: '))
    listval.append(val)
    count += 1
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar [S/N]: ')).strip().upper()
    if continuar in 'Nn':
        break
print(f'A liste tem {count} elementos')
listval.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {listval}')
if 5 in listval:
    print(f'O valor 5 faz parte da lista')
else:
    print(f'O valor 5 não faz parte da lista')
'''
#........................ exercitar .................................
listnum = []
count = 0
while True:
    listnum.append(int(input('Digite um valor: ')))
    listnum.sort(reverse=True)
    count += 1
    while True:
        continuar = str(input('Quer continuar [S/N]: ')).upper()
        if continuar in "NS":
            break
    if continuar == "N":
        break
print(f'Você digitou {count} elementos.')
print(f'Os valores em ordem decrescencte são {listnum}')
if 5 in listnum:
    print('O valor 5 está presente na nossa lista. ')
else:
    print('o valor 5 não está presente na nossa lista. ')















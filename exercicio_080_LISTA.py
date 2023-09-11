'''
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os
em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre
a lista ordenada na tela.
'''
'''
listanum = []
maior = menor = 0
for c in range(0, 5):
    num = int(input('digite um numero: '))
    listanum.append(num)
    if c == 0:
        maior = menor = listanum[c]
        print('Adicionado no final da lista')
    else:
        if listanum[c] < maior:
            print('Adicionado na pocição 0 da lista')
        if listanum[c] >menor:
            print('Adicionado no fim da lista')
print(listanum)

'''

#.............................. exercitar..................................
listnum = []
for c in range(0, 5):
    num = int(input('Digite um número: '))
    if c == 0 or num > listnum[-1]:
        listnum.append(num)
        print(f'Valor adicionado no final da lista...')
    else:
        pos  = 0
        while pos < len(listnum):
            if num <= listnum[pos]:
                listnum.insert(pos, num)
                print(f'O valor foi inserido na posição {pos} ...')
                break
        pos += 1
print('-='*30)
print(f'Os valores digitados na lista são {listnum}')














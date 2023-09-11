'''
faça um programa que leia 5 valores numericos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menos valor digitado e as suas respetivas
posições na lista
'''
'''
maior = menor = 0
listanun = []
for c in range(0, 5):
    num = int(input(f'digite um valor na posição {c}: '))
    listanun.append(num)
    if c == 0:
        maior = menor = listanun[c]
    else:
        if listanun[c] > maior:
            maior = listanun[c]
        if listanun[c] < menor:
            menor = listanun[c]
print('-='*30)
print(f'Você digitou os valores {listanun}')
print(f'O menor valor é {menor} está na posição ',end='')
for p, c in enumerate(listanun):
    if c == menor:
        print(f' {p}...\n', end='')
print(f'O maior valor é {maior} está na posição ',end='')
for p, c in enumerate(listanun):
    if c == maior:
        print(f' {p}...', end='')
        
'''

#.......................... Praticando ............................
lintnum = []
mai = men = 0
for c in range(0, 5):
    lintnum.append(int(input(f'Digite um valor na posição {c}: ')))
    if c == 0:
        mai = men = lintnum[c]
    else:
        if lintnum[c] > mai:
            mai = lintnum[c]
        if lintnum[c] < men:
            men = lintnum[c]
print('-='*30)
print(f'Você acabou de digitar os valores {lintnum}.')
print(f'O maior valor digitado foi {mai}. Que está na posição ',end='')
for i, v in enumerate(lintnum):
    if v == mai:
        print(f'{i}...',end='')
print(f'\nO menor valor digitado foi {men}. Que está na posição ',end='')
for i, v in enumerate(lintnum):
    if v == men:
        print(f'{i}...',end='')


























'''Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.


matriz = [[0,0,0], [0,0,0], [0,0,0]]
count = soma_col = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = (int(input(f'Digite um valor para [{l}, {c}]: ')))
        if matriz[l][c] % 2 == 0:
            count += matriz[l][c]
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-='*30)
print(f'A soma dos valores pares são {count}')
for l in range(0, 3):
    soma_col += matriz[l][c]
print(f'A soma da coluna 3 é {soma_col}')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    else:
        if matriz[1][c] > maior:
            maior = matriz[1][c]
print(f'O maior valor na linha 2 é {maior}')

'''
#------------------------- Exercitando -------------------------------------


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = soma_col_3 = maior =  0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l] [c] = int(input(f'Digite os valores da matriz na posição [{l}, {c}]: '))
        if matriz[l] [c] % 2 == 0:
            soma += matriz [l] [c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]',end=' ')
    print()
print(f' A soma de todos os valores pares na matriz é de  {soma}.')
for l in range(0, 3):
    soma_col_3 += matriz[l] [2]
print(f'A soma de todos os valores na última coluna é de {soma_col_3}.')
for c in range(0, 3):
    if c == 0:
        maior = matriz [1] [c]
    else:
        if matriz[1] [c] > maior:
            maior = matriz[1] [c]
print(f'O maior valor da segunda linha é {maior}')













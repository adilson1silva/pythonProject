'''
Crie um programa que leia uma frase qualquer e diga se ela é um
palíndromo, desconsiderando os espaços.

Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA,
O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
'''


frase = str(input('Digite um nome: ')).upper().strip()
frase_m = frase.split()
juntar = ''.join(frase_m)
inverso = ''
print(f'{juntar} vs ',end='')
for c in range(len(juntar) - 1, -1, -1):
    inverso += juntar[c]
print(inverso)
if juntar == inverso:
    print('\né um polindromo')
else:
    print('\nnão é um polindromo')
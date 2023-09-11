'''
Faça um programa que leia o peso de cinco pessoas. No final,
mostre qual foi o maior e o menor peso lidos.
'''
maior_peso = 0
menos_peso = 0
count = 0
for c in range(0, 5):
    peso = float(input('Digite o peso: '))
    count += 1
    if count == 1:
        menos_peso = peso
        maior_peso = peso
    elif c > maior_peso:
        maior_peso = peso
    elif c < menos_peso:
        menos_peso = peso
print(f'o maior peso digitado foi de {menos_peso} kg')
print(f'O menor peso digitado foi de {maior_peso} kg')

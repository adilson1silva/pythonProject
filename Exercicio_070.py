'''
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
'''

print('-'*15)
print('LOJA SUPER BARATÃO')
print('-'*15)
total_preço = count = menor_preço = count1 = 0
while True:
    nome = str(input('Nome do produto: '))
    preço = int(input('Preço R$: '))
    total_preço += preço
    count1 += 1
    if count1 == 1:
        menor_preço = preço
    elif preço < menor_preço:
        menor_preço = preço
    if preço > 1000:
        count += 1
    while True:
        continuar = str(input('Quer continuar [S/N]: ')).upper()
        if continuar in 'NS':
            break
    if continuar == 'N':
        break
print(f'O total da compra foi de R${total_preço:.2f}')
print(f'Temos {count} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi lapiseira que custa R${menor_preço:.2f}')


'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos
preços, na sequência. No final, mostre uma listagem de preços, organizando os dados
em forma tabular.


produtos = ('caderno', 1.55, 'lapis', 0.80, 'baracha', 0.50, 'muchila', 7.00,
            'sapato', 30.00, 'caneta', 1.00)
print('-'*30)
print(f'{"Listagem de produto":^30}')
print("-"*30)

for c in range(0, len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c]:.<30}',end='')
    elif c % 2 != 0:
        print(f'$ {produtos[c]:>7.2f}')
print("-"*30)

'''
#---------------------------------------------------------------------

produtos = ('caderno', 1.55, 'lapis', 0.80, 'baracha', 0.50, 'muchila', 7.00,
            'sapato', 30.00, 'caneta', 1.00)
print('-'*40)
print(f'{"listagem de preços":^40}')
print('-'*40)
for item in range(0, len(produtos)):
    if item % 2 == 0:
        print(f'{produtos[item]:.<30}',end=' ')
    else:
        print(f'R$  {produtos[item]:.2f}')

















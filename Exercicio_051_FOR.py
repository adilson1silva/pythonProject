'''
 Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
 No final, mostre os 10 primeiros termos dessa progressão.
'''

print('='*30)
print('    10 TERMOS DE UMA PA')
print('='*30)
pri_termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = pri_termo + (10 - 1) * razão
for c in range(pri_termo, décimo, razão):
    print(c, end='-> ')
print('\n Acabou!')


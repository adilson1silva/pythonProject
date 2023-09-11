'''
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''

print('Gerador de uma PA')
print('-='*10)
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
count = 0
res = p
print(f'{p}',end='')
while count < 9:
    res += r
    print(f'{res}',end=' -> ')
    count += 1
print('FIM!')
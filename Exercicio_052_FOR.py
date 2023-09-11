'''
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''
count = 0
num = int(input('Digite um número: '))
for c in range(1, num + 1, 1):
    if num % c == 0:
        print(f'\033[35m{c}',end=' ')
        count += 1
    else:
        print(f'\033[32m{c}',end=' ')
if count == 2:
    print(f'\n\033[35m O número {num} é primo!')
else:
    print(f'\n\033[32m O número {num} não é primo!')
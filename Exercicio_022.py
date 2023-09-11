'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas
- o nome com todas as letras minúsculas
- quantas letras ao todos (sem considerar espaços)
- quantas letras tem o primeiro nome
'''

nom = str(input('Digite um nome completo: ')).strip()

print('---------------RESULTADOS----------------')
print('O nome com todas as letras maiúsculas é: ')
print(f'\033[0;34m{nom.upper()}\033[0;0m')
print('O mone com todas as letras minúsculas é:')
print(f'\033[0;34m{nom.lower()}\033[0;0m')
print('O nome completo (sem considerar espaço é contituido por: )')
print(f'\033[0;34m{len(nom.replace(" ", ""))} letras\033[0;0m')
print('o primeiro nome é composto por:')
print(f'\033[0;34m{len(nom.split()[0])} letras')

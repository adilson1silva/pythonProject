'''
crie um programa que leia o nome de uma pessoa e diga se ele tem "silva" no
nome.
'''


nom = str(input('Digite um nome: ')).lower()
c_nom = nom.split()
print(f'O nome é composto por silva? {"silva" in c_nom}')
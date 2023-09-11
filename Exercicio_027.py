'''
Faça um programa que leia um nome completo de uma pessoa. Mostrando em seguida o
primeiro e o último nome separadamente.
'''


nom = str(input('Digite o nome completo: '))
c_nom = nom.split()
print(f'Primeiro nome = {c_nom[0]}')
print(f'Último nome = {nom[len(nom)-1]}')
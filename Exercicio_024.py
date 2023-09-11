'''
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com
o nome santa
'''


nom = str(input('Digite o nome da sua cidade: '))
p_nom = nom.split()[0]
print(f'A minha cidade começa com palavra santa? {"santo" in p_nom}')
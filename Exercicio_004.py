'''
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
e todas as informações possíveis sobre ele.
'''

a = input('Digite algo: ')
print(f'Que tipo é: {type(a)}')
print(f'Contém apenas espaços? {a.isspace()}')
print(f'É numerico? {a.isnumeric()}')
print(f'É minuscula? {a.islower()}')
print(f'É maiuscula? {a.isalpha()}')
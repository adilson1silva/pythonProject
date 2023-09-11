'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''

#sexo = ' '
sexo = str(input('digite o seu sexo: '))
while sexo not in 'MmFf':
    sexo = str(input('dados imvalidos por favor informe o seu sexo: : '))
print(f'sexo {sexo.upper()} registado com sucesso')

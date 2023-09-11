'''
Faça um exercício que leia o comprimento do cateto oposto e do cateto adjacente
de um triângulo. Calcule e mostre o comprimento da hipotenusa
'''



import math
cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
print(f'A hipotenuza é igual a {hipotenusa:.2f} ')

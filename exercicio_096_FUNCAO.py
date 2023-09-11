'''
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um
terreno retangular (largura e comprimento) e mostre a área do terreno.
'''

def área(larg, comp):
    área = larg * comp
    print(f'A área do terreno com largura {larg}m e comprimento {comp}m é de {área}m^2')

#programa principal
l = float(input('Digite a largura do terreno: '))
c = float(input('Digite o comprimento do terreno: '))
área(l, c)

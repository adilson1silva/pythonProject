'''
O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos
dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem
sorteada.
'''


import random
n1 = str(input('Digite um nome: '))
n2 = str(input('Digite outro nome: '))
n3 = str(input('Digite mais um nome: '))
n4 = str(input('Digite o último nome: '))
lista  =[n1, n2, n3, n4]
random.shuffle(lista)
print(f'A ordem de apresentação foi {lista}.')
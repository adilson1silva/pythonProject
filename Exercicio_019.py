'''
Um professor quer sortiar um dos quatro alunos para apagar o quadro. Faça um
programa que ajude ele, lendo o nome deles e escolhendo o nome escolhido.
'''



import random
n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Treceiro nome:'))
n4 = str(input('Quarto nome'))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print(f'Os quatro alunos são: {escolhido}')

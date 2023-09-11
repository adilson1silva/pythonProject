'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do
seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para
os inferiores ou iguais, o aumento é de 15%.
'''

sal = int(input('Qual o seu salário: R$'))
if sal >= 1250:
    aumento = sal * 0.1
    print(f' Quem ganhava R${sal:.2f} passa a garar R${sal + aumento:.2f} ')
else:
    aumento = sal * 0.15
    print(f'Quem ganhava R${sal:.2f} passa a ganhar R${sal + aumento:.2f}')
'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''

val_casa = int(input('Qual o valor da casa? '))
sal_comprador = int(input('Qual o salário do comprador? '))
ano_paga = int(input('Em quantos anos deseja pagar a casa? '))
n_meses = ano_paga * 12
pre_mensal = val_casa / n_meses
print(f'Para para uma casa de R${val_casa} em {ano_paga} anos a prestação será de R${pre_mensal:.2f}')
if pre_mensal > (sal_comprador*0.3):
    print('\033[0;35mEmprestimo NEGADO!')
else:
    print('\033[0;34mEmprestimo CONCEDIDO!\033[0;0m')
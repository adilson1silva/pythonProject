'''
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros
'''

produto = int(input('Qual o preço do produto?[R$]: '))
print('-------------- Como deseja fazer o pagamento: -------------------\n'
      '[1] à vista dinheiro/cheque\n'
      '[2] à vista no cartão\n'
      '[3] em até 2x no cartão\n'
      '[4] 3x ou mais no cartão\n'
      '------------------------------------------------------------------')
opção = int(input('Qual o modo de pagamento: '))
if opção == 1:
    print(f'O preço do produto encluindo o descolto fico por {(produto * 0.1) - produto:.2f}')
elif opção ==2:
    print(f'O preço do produto encluindo o descolto fico por {(produto * 0.05) - produto:.2f}')
elif opção == 3:
    print(f'O preço do produto encluindo o descolto fico por {produto:.2f}')
elif opção == 4:
    quantas =int(input('Em quantas parcelas quer pagar? '))
    print(f'Sua compra será parcelada em {quantas}x de {((produto * 0.2) + produto) / quantas:.2f} com juros\n'
          f'Sua cmpra de {produto:.2f} vai custar {(produto * 0.2) + produto:.2f}')



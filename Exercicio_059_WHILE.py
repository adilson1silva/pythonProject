'''
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''

opção = 0


num_1 = int(input('Primeiro número: '))
num_2 = int(input('Segundo número: '))
while opção != 5:
    print('[1] somar\n'
          '[2] multiplicar\n'
          '[3] Maior\n'
          '[4] novos números\n'
          '[5] sair do programa\n')
    opção = int(input('Qual a sua opição: '))

    if opção == 1:
        print(f'A soma entre {num_1} + {num_2} é {num_1 + num_2}')
        print('=-' * 30)
        opção = int(input('Qual a sua opição: '))
    if opção == 2:
        print(f'A multiplicação entre {num_1} * {num_2} é {num_1 * num_2}')
        opção = int(input('Qual a sua opição: '))
    if opção == 3:
        if num_1 > num_2:
            print(f'O número {num_1} é maior do que o {num_2}')
            opção = int(input('Qual a sua opição: '))
        elif num_1 == num_2:
            print(f'O número {num_1} é igual ao número {num_2}')
            opção = int(input('Qual a sua opição: '))
        else:
            print(print(f'O número {num_2} é maior do que {num_1}'))
            opção = int(input('Qual a sua opição: '))
        if opção == 4:
            other_num_1 = int(input('Primeiro número: '))
            other_num_2 = int(input('Segundo número: '))
            num_1 = other_num_1
            num_2 = other_num_2
        if opção == 5:
            print('OBRIGADO! E volte sempre!')



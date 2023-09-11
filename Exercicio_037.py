'''
Escreva um programa em Python que leia um número inteiro qualquer e peça
para o usuário escolher qual será a base de conversão:
1 para binário,
2 para octal e
3 para hexadecimal.
'''

num = int(input('Digite um número inteiro: ' ))
print('Escalha uma base de converção:\n'
      '[1] para fazer a conversão para binário\n'
      '[2] para fazer a converção para actal\n'
      '[3] para fazer a converção para hexadecimal\n')
opção = int(input('Digite a sua opção: '))
if opção == 1:
    print(f'O valor {num} comvertido para binário é \033[0;34m{bin(num)[2:]}\033[0;0m ')
elif opção == 2:
    print(f'O valor {num} convertido para octal é \033[0;34m{oct(num)[2:]}\033[0;0m')
else:
    print(f'O valor {num} convertido para hexadecimal é \033[0;34m{hex(num)[2:]}\033[0;0m')

'''
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final
quantos palpites foram necessários para vencer.
'''

from random import randint

count = 1
computador = randint(0, 10)
jogador = int(input('Digite um número [0, 10]: '))
while jogador != computador:
    count += 1
    if jogador < computador:
        print(f'Mais... Tente novamente!')
    elif jogador > computador:
        print(f'Menos... Tente novamente')
    jogador = int(input('Não acertou! Digite novamente: '))

print('=' * 30)
print(f'O computador digitou o número {computador}')
print(f'Você fez {count} tentativas até acertar')

'''
Crie um programa que faça o computador jogar Jokenpô com você.
'''
from random import randint
from  time import sleep
itens = ('Pedra', 'papel', 'tesoura')
comtputador = randint(0, 2)
print('Suas opções:\n'
      '[ 0 ] PEDRA\n'
      '[ 1 ] PAPEL\n'
      '[ 2 ] TESOURA\n')
jogador = int(input('Qual a sua jogada: '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ')
sleep(0.5)
if comtputador == 0:
    if jogador == 0:
        print(f'O computador jogou {itens[comtputador]} e você jogou {itens[jogador]}\n '
              f'ouvi um impate')
    elif jogador == 1:
        print(f'O computador jogou {itens[comtputador]} e você jogou {itens[jogador]}\n '
              f'você ganhou o jogo')
    elif jogador == 2:
        print(f'O computador jogou {itens[comtputador]} e você jogou {itens[jogador]}\n '
              f'computador ganhou o jogo')
elif comtputador == 1:
    if jogador == 1:
        print(f'O computador jogou {itens[comtputador]} e você jogou {itens[jogador]}\n '
              f'ouvi um impate')
    elif jogador == 0:
        print(f'O computador jogou {itens[comtputador]} e você jogou {itens[jogador]}\n '
              f'computador ganhou o jogo')
    elif jogador == 2:
        print(f'O computador jogou {itens[comtputador]} e você jogou {itens[jogador]}\n '
              f'você ganhou o jogo')

elif comtputador == 2:
    if jogador == 2:
        print(f'O computador jogou {itens[comtputador]} e você jogou {itens[jogador]}\n '
              f'ouvi um impate')
    elif jogador == 0:
        print(f'O computador jogou {itens[comtputador]} e você jogou {itens[jogador]}\n '
              f'você ganhou o jogo')
    elif jogador == 1:
        print(f'O computador jogou {itens[comtputador]} e você jogou {itens[jogador]}\n '
              f'computador ganhou o jogo')


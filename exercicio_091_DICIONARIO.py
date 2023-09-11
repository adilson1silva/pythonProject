'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário
em ordem, sabendo que o vencedor tirou o maior número no dado.


from random import randint
from time import sleep
from operator import itemgetter
jogos = {
    'jogador1': randint(0, 6),
    'jogador2': randint(0, 6),
    'jogador3': randint(0, 6),
    'jogador4': randint(0, 6)
}
ranking = {}
for k, v in jogos.items():
    sleep(0.5)
    print(f'O {k} tirou {v} do dado')
print('-'*30)
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    sleep(0.5)
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
'''


#-------------------- Exercitanto ------------------------

from random import randint
from time import sleep
from  operator import itemgetter
jogar = {'Jogador 1': randint(1, 6),
         'Jogador 2': randint(1, 6),
         'Jogador 3': randint(1, 6),
         'Jogador 4': randint(1, 6)}
ranking = []
ranking = sorted(jogar.items(), key=itemgetter(1), reverse=True)
for k, v in jogar.items():
    print(f'{k}: {v}')
    sleep(1)
print('== RANKING DOS JOGADORES ==')
for k, v in enumerate(ranking):
    print(f'Em  {k + 1}º lugar está o {v[0]} com {v[1]} pontos')


















'''
 Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um
 sistema de visualização de detalhes do aproveitamento de cada jogador.
'''


time = []
jogador = {}
partida = []

while True:
    jogador.clear()
    jogador["nome"] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
    partida.clear()
    for c in range(0, tot):
        partida.append(int(input(f'Quantos gols na partida {c + 1}? ')))
    jogador["gols"] = partida[:]
    jogador["total"] = sum(partida)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar [S/N]')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO. Responda [S/N]')
    if resp == "N":
        break
print('-=' * 40)
print('cod ',end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k + 1:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print(f'-=' * 40)
while True:
    busca = int(input('Motrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Não existe jogador com codigo de {busca}!')
    else:
        print(f'Levantamento do jogador {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'      No jogo {i + 1} fez {g} gols.')
    print('-'*40)
print('<< VOLTE SEMPRE >>')


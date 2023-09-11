'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa
vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de
gols feitos em cada partida. No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato.


dados = {}
partidas = []
dados['Nome'] = str(input('Nome: '))
n_part = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
total = 0
for a in range(1, n_part+1):
    p = int(input(f'Quantos gols na partida {a}? '))
    partidas.append(a)
    dados['gols'] = partidas
    total += p
dados['soma'] = total
print('-='*30)
print(dados)
print('-='*30)
for k, v in enumerate(dados.items()):
    print(f'{k} O campo {v[0]} tem o valor {v[1]}.')
print('-='*30)
print(f'O jogador {dados["Nome"]} jogou {n_part} partidas.')
for k, v in enumerate(partidas):
    print(f'    => Na partida {k}, fez {v} gols.')
print(f'Foi um total de {dados["soma"]} gols.')
'''


#------------------------- Exercitando ------------------------

dados  = {}
dados_gols = []
tot = 0
dados["Nome"] = str(input('Digite o nome do jogador: '))
n_partidas = int(input(f'Quantas partidas o {dados["Nome"]} jogou? '))
for c in range(0, n_partidas):
    num_gol = int(input(f'Quantas gols na partida {c}: '))
    tot += num_gol
    dados_gols.append(num_gol)
dados["gols"] = dados_gols[:]
dados["total"] = tot
print('-='*30)
print(dados)
print('-='*30)
for k, v in dados.items():
    print(f'- O campo {k} têm o valor {v}')
print('-='*30)
print(f'O jogador {dados["Nome"]} jogou {n_partidas} partidas.')
for i, c in enumerate(dados_gols):
    print(f'Na partida {i} marcou {c}')
print(f'Foi um total de {tot}')




















'''
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros
opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser
capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado
corretamente.
'''

nome = str(input('Digite o nome do jogador: '))
gol = int(input('Digite o número de gols marcado: '))
if nome is not str:
    nome = '<desconhecido>'
print(f'O jogador {nome} marcou {gol} gols.')



























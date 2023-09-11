'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai
perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada
jogo, cadastrando tudo em uma lista composta.


from random import randint
quant = int(input('quantos jogos você quer sortiar? '))
lista = []
jogos = []
total = 1
while total <= quant:
    count = 0
    while True:
        a = randint(1, 60)
        if a not in lista:
            count += 1
            lista.append(a)
        if count == 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
for i, l in enumerate(jogos):
    print(f'jogos {i}: {l}')


'''
# ----------------------------- exercitanto ---------------------------
print('-='*20)
print(f'{"        JOGA NA MAGA SENA"}')
print('-='*20)
lista = []
jogo = []
from random import randint
from time import sleep
quantos = int(input('Quantos jogos você quer sortiar? '))
count_total = 0
while count_total < quantos:
    count = 0
    while True:
        num = randint(0, 60)
        if num not in lista:
            lista.append(num)
            count += 1
        if count == 6:
            break
    lista.sort()
    jogo.append(lista[:])
    lista.clear()
    count_total += 1
for i , l in enumerate(jogo):
    sleep(1)
    print(f'Jogo {i}:  {l}')














'''
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando
o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''


from random import randint
soma = count = 0
print('-='*15)
print('VAMOS JOGAR PAR OU IMPAR')
print('-='*15)
while True:
    val = int(input('Qual o valor: '))
    conputador = randint(0, 10)
    tipo = str(input('Par ou Impar? [P/I] ')).upper()
    while True:
        if tipo not in "PI":
            tipo = str(input('Par ou Impar? [P/I] ')).upper()
        elif tipo in "PI":
            break
    soma = val + conputador
    if tipo == 'P':
        if soma % 2 == 0:
            print(f'O computador jogou {conputador} e você jogou {val}. Resultado final par')
            count += 1
        else:
            print(f'O computador jogou {conputador} e você jogou {val}. IMPAR, você perdeu. GAME OVER')
            break
    if tipo == 'I':
        if soma % 2 != 0:
            print(f'O computador jogou {conputador} e você jogou {val}. Resultado final impar')
            count += 1
        else:
            print(f'O computador jogou {conputador} e você jogou {val}. PAR, você perdeu. GAME OVER')
            break
print(f'você ganhou {count} vezes até perder')



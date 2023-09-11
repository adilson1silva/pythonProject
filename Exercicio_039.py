'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
 se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou
 do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
'''

from datetime import date
ano_nanc = int(input('Digite o ano do seu nascemento: '))
idade = date.today().year - ano_nanc
if idade > 18 and idade < 40:
    print(f'Você está com {idade} anos de já deveria ter alistado\n'
          f'deveria alistar em {ano_nanc + 18}\n')
elif idade == 18:
    print(f'Você está com {idade} anos\n'
          f'deve alistar imediatemente\n')
elif idade < 18:
    print(f'Você está com {idade} anos ainda não deve se alistar\n'
          f'deverá alistar em {ano_nanc+18}\n')

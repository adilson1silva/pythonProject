'''
A Confederação Nacional de Natação precisa de um programa que leia o ano de
nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER
'''

from datetime import date
ano_nascemento = int(input('Digite o ano do seu nascemento: '))
data_atual = date.today().year
idade = data_atual - ano_nascemento
print(f'---------------RESULTADOS--------------')
if idade <= 9:
    print(f'\033[0;34mTens {idade} anos \nA sua categoria é MIRIM \033[0;0m')
elif idade > 9 and idade <= 19:
    print(f'\033[0;34mTens {idade} anos \nA sua categoria é JÚNIOR\033[0;0m')
elif idade >19 and idade <= 25:
    print(f'\033[0;34mTens {idade} anos \nA sua categoria é SÊNIOR \033[0;0m')
else:
    print(f'\033[0;34mTens {idade} anos \nA sua categoria é MASTER\033[0;34m')
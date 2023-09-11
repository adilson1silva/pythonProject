'''
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro
o ano de nascemento de uma pessoa, retornando um valor literal incicando se uma pessoa
tem voto NEGADO, OPCIONAL, OU OBRIGATÓRIO nas eleições
'''

def voto():
    from datetime import date
    data_atual = date.today()
    ano_atual = data_atual.year
    idade = ano_atual - d_nasc

    if idade < 18:
        return(f'Você tem {idade} anos por isso não pode votar')
    elif idade >= 18 and idade <= 65:
        return(f'Você tem {idade} anos, é obrigatório votar')
    else:
        return(f'você tem {idade} anos, o seu voto é facultativo')


#programa principal
print('-='*30)
d_nasc = int(input('Digite a data de nacimento: '))
n = print(voto())















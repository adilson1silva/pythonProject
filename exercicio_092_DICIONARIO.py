'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o
(com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário
receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade,
com quantos anos a pessoa vai se aposentar.


from datetime import datetime
dados = {}
dados['nome'] = str(input('N0me: '))
dados['D.nasc'] = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - dados['D.nasc']
dados['C.trabalho'] = int(input('Carteira de trabalho [0 não tem]: '))
if dados['C.trabalho'] == 0:
    print('-'*30)
    for k, v in dados.items():
        print(f'{k} tem o valor {v}')
else:
    dados['Ano.contr'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('salário: '))
    dados['aposento'] = dados['idade'] + ((dados['Ano.contr'] + 35) - datetime.now().year)
    print('-' * 30)
    for k, v in enumerate(dados.items()):
        print(f'{k}: {v[0]} tem o valor {v[1]}')
   '''

#---------------------- Exercitando ----------------
from datetime import date
dados = {}
dados["Nome"] = str(input('Nome: '))
data_nascimento = int(input('Ano de nascimento: '))
dados["nascimento"] = date.today().year - data_nascimento
dados["C.T"] = int(input('Carteira de trabalho [0 não têm]: '))
if dados["C.T"] != 0:
    dados["contratação"] = int(input(('Ano de contratação: ')))
    dados["salario"] = int(input('Salario: '))
    dados["aposentadoria"] = (dados["contratação"] - data_nascimento) + 35
print("-="*20)
for k, v in dados.items():
    print(f'- {k} tem o valor {v}')





















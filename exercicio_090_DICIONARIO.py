'''
Faça um programa que leia nome e média de um aluno, guardando também a situação em um
 dicionário. No final, mostre o conteúdo da estrutura na tela.


dados = {}
dados['nome'] = str(input('Nome: '))
dados['média'] = float(input('Média: '))
if dados['média'] >= 10:
    dados['situação'] = 'Aprovado'
elif dados['média'] > 10 and dados['média'] < 13:
    dados['situação'] = 'recuperação'
else:
    dados['situação'] = 'reprovado'
print('='*30)
for k, v in dados.items():
    print(f'O {k} é igual a {v}')
'''
#------------------------ Exercitando ----------------------------
aluno = {}
aluno["Nome"] = str(input('Nome: '))
aluno["Média"] = float(input(f'Média do {aluno["Nome"]}: '))
print('-='*15)
for k, v in aluno.items():
    print(f' {k}: {v}')
if aluno["Média"] >= 7.5:
    print('Aluno aprovado')
elif aluno["Média"] < 5:
    print('Aluno reprovado')
else:
    print('Aluno em fase de recuperação')



















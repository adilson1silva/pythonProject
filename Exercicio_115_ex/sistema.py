from Exercicio_115_ex.lib.interface import *
from Exercicio_115_ex.lib.arquivo import *
from time import sleep

arq = 'Cursoemvideo.txt'

if not arquivoExiste(arq):
    criaArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar novas pessoas', 'sair do sisrema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Listar pessoas')
    elif resposta == 4:
        cabeçalho('sair do sitema... volte sempre!')
        break
    else:
        print(f'\033[31mERRO! Digite um número valido.\033[m')
    sleep(2)

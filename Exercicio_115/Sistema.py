from Exercicio_115.lib.interface import *
from Exercicio_115.lib.arquivo import *
from time import sleep

arp = 'cursoemvideo.txt'

if not arquivoExiste(arp):
    criarArquivo(arp)

while True:
    resposta = menu(['ver pessoas cadastradas', 'cadastrar novas pessoas', 'sair do sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo!
        lerArquivo(arp)
    elif resposta == 2:
        # Cadartrar uma nova pessoa.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arp, nome, idade)
    elif resposta == 3:
        # Opção de sair do sistema
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        # Digitou uma opção errada no menu.
        print('\033[31mERRO! Digite uma opção válida! \033[m')
    sleep(2)
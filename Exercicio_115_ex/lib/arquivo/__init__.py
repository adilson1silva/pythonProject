from Exercicio_115_ex.lib.interface import *


# Verificar se o arquivo existe
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

# Criar arquivo novo
def criaArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Ouve um ERRO na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso')


# Ler arquivo
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        print(a.read())
    finally:
        a.close()


# cadastrar novas pessoas
def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(nome, 'at')
    except:
        print('Ouve um erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('ouvw um ERRO na hora de escrever os dados ')
        else:
            print(f'Novo rigistro de {nome} adicionado')
            a.close()



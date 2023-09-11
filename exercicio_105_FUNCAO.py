'''
Faça um programa que tenha uma função notas() que pode receber várias notas de
alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
'''

def notas(* nota,sit=False):
    """
    :param nota:Uma ou mais notas do aluno (aceita vários)
    :param sit:valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    Programa criado por Adilson Silva
    """
    d_principal  = {}
    d_principal["total"] = len(nota)
    d_principal["maior"] = max(nota)
    d_principal["menor"] = min(nota)
    média = sum(nota)/len(nota)
    d_principal["média"] = média
    if sit:
        if média < 5:
            d_principal["situação"] = 'Situação ruim'
        elif média > 7:
            d_principal["situação"] = 'situação muito bom'
        else:
            d_principal["situação"] = 'Situação rasuavel'
    return d_principal


#Programa principal
resp = notas(5.5, 9.5, 10, 6.5,sit=True)
print(resp)
help(notas)
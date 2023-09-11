'''
Faça um programa que tenha uma função chamada escreva(), que receba um texto
qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
'''


def escreva(txt):
    print('-' * (len(txt) + 4))
    print(f'  {txt}')
    print('-' * (len(txt) + 4))

#programa principal
escreva('Adilson Mendes Silva')
escreva('Estou aprendendo python')
escreva('tenho de evoluir nesta linguagem de programação')





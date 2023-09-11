'''
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).0 Depois
 disso, você deve mostrar, para cada palavra, quais são as suas vogais.


palavras = ('lalis', 'caneta', 'boracha', 'pincel', 'quadro', 'vasoura')
for c in range(0, len(palavras)):
    print(f'\n Na palavra {palavras[c]} temos:')
    for letras in palavras[c]:
        if letras.lower() in 'aeino:':
            print(f'{letras}',end='')

'''

#-----------------------------------------------------------

palavras = ('lapis', 'caneta', 'boracha', 'pincel', 'quadro', 'vasoura')
for p in range(0, len(palavras)):
    print(f'\nNa palavra {palavras[p]} temos',end=' ')
    for vogais in palavras[p]:
        if vogais in 'aeiou':
            print(vogais, end=' ')
















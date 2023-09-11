'''
Faça um programa que tenha uma função chamada contador(), que receba três
parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através
da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
'''


from time import sleep
def contador(inic, fim, pas):
    if inic < fim:
        val = inic
        print(f'{val}', end=' ')
        while val < fim:
            if pas <= 0:
                pas = 1
            val += pas
            if val < fim:
                sleep(0.2)
                print(f'{val}', end=' ')

    if inic > fim:
        print('=-' * 30)
        val = inic
        print(f'{val}', end=' ')
        while val > fim:
            if pas <= 0:
                pas = 1
            val -= pas
            sleep(0.2)
            print(f'{val}', end=' ')
        print('FIM!')


#programa principal
print('Personalizar a contagem')
i = int(input('Inicio: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))
contador(i, f, p)
print('=-' * 30)






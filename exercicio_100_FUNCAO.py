'''
Faça um programa que tenha uma lista chamada números e duas funções chamadas
sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los
dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares
sorteados pela função anterior.

'''
lista = []

def números():
    from random import randint
    count = 0
    while count < 5:
        num = randint(1, 20)
        if num not in lista:
            lista.append(num)
            count +=1
    print(lista)

def SomaPar():
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'A soma dos valores pares é de {soma}')

# Programa principal
números()
SomaPar()





'''
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante
'a função input() do Python, só que fazendo a validação para aceitar apenas um valor
numérico.
Ex: n = leiaInt('Digite um n: ')
'''
def leiaInt(num):
    ok = False
    while True:
        num = str(input('Digite um número: '))
        if num.isnumeric():
            num = int(num)
            ok = True
        else:
            print(f'\033[0;33mERRO! Digite um número inteiro válido.\033[m')
        if ok == True:
            break
    return num


#Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
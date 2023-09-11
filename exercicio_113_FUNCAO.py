'''
Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo
agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie
também uma função leiaFloat() com a mesma funcionalidade.
'''
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[33mO utilizador preferiu não digitar o número\033[m')
            return 0
        else:
            return n

        
def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO! Digite um número real válido.')
            continue
        except(KeyboardInterrupt):
            print('\033[31mO utilizador preferiu não digitar o valor.')
            return 0
        else:
            return n

#programa principal
n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real: ')
print(f'Vocês digitou o número {n1} e {n2}')
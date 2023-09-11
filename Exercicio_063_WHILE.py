'''
Escreva um programa que leia um número N inteiro qualquer e
mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8
'''

print('-='*20)
print('Sequencia de Fibonate')
print('-='*20)
primeiro_termo = 0
segundo_termo = 1
q_termos = int(input('Quantos termos você quer mostrar? '))
count = 2
while count < q_termos:
    resultado = primeiro_termo + segundo_termo
    print(resultado, end=' -> ')
    primeiro_termo = segundo_termo
    segundo_termo = resultado
    count += 1
print('Fim')

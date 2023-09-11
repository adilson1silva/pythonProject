'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai
parar quando o usuário digitar o valor 999, que é a condição de parada. No final,
mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''
count = 0
soma = 0
while True:
    num  = int(input('Digite um número: '))
    if num == 999:
        break
    count += 1
    soma += num
print(f'Foram digitados {count} números.')
print(f'A soma dos números digitados foi de {soma}')
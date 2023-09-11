'''
Faça um programa que calcule a soma entre todos os números que são múltiplos
de três e que se encontram no intervalo de 1 até 500.
'''
s = 0
count = 0
for c in range(1, 501):
    if c % 2 != 0:
        if c % 3 == 0:
            count += 1
            s += c
print(f'A soma entre os {count} números solicitados é de {s}')



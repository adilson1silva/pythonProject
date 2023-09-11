'''
Faça um programa que leia uma frase pelo teclado e mostre:

- quantas vezes aparece a letra "A".
- Em que posição ele aparece a primeira vez.
- em que posição ela aparece a última vez.
'''

frase = str(input('Digite uma frase: ')).upper()
print('---------RESULTADOS----------')
print('A letra "A" apareçe: ')
print(f'\033[0;34m{frase.count("A")} vezes \033[0;0m')
print('A primeira letra "A" está na posição:')
print(f'\033[0;34m{frase.find("A")+1}ª posição\033[0;0m')
print('A última letra "A" está na posição: ')
print(f'\033[0;34m{frase.rfind("A")}ª posição\033[0;0m')

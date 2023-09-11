'''
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
'''

nota1 = float(input('Digete a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota2 + nota1) / 2
print('-------------RESULTADOS---------------')
if media < 10.0:
    print(f'\033[0;31mA sua nota final foi de {media} você foi REPROVADO\033[0;0m')
elif media >10 and media <= 13:
    print(f'\033[0;34mVovê foi APROVADO, mas está em fase de recuperação\033[0;0m')
else:
    print(f'\033[0;34m você foi APROVADO\033[0;0m')
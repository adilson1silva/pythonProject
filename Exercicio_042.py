'''
Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de
mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
'''

pri_segmento = float(input('Digite o primeiro segmento: '))
seg_segmento = float(input('Digite o segundo segmento: '))
ter_segmento = float(input('Digite o terceiro segmento: '))
print('---------------RESULDADOS---------------------')
if pri_segmento == seg_segmento == ter_segmento:
    print(f'\033[0;31mO s segmentos acima podem formar um TRIÂNGULO EQUILÁTERO\033[0;0m')
elif pri_segmento != seg_segmento != ter_segmento:
    print(f'\033[0;31mOs segmentos acima podem formar um TRIÂNGULO ESCALENO\033[0;0m')
else:
    print(f'\033[0;31mOs segmentos acima podem formar um TRIÂNGULO ISÓSCELES\033[0;0m')
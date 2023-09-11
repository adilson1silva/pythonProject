'''
Manipulação de string
len(frase)       - ver o tamanho do string
frase.strip()    - Remove espaço no inicio e no fim
frase.count('o') - contar quantos 'o' que estão na frase
'Curso' in frase - perguntar se a palavra 'Curso' está em frase
frase.split()    - vai divider a frase em cada palavra
'''

frase = 'Curso em vídeo Python'
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[1:15:2])
print(frase.count('o'))
print(len(frase))
print(frase.strip())
print(frase.replace('Python', 'Android'))
print('Curso' in frase)
print(frase.find('vídeo'))
print(frase.split())

dividido = frase.split()
print(dividido[2] [3])
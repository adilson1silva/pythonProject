'''
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os
em uma lista única que mantenha separados os valores pares e ímpares. No final,
mostre os valores pares e ímpares em ordem crescente.

l_principal = []
l_par = []
l_impar = []
for c in range(0, 7):
    val = int(input(f'digite o {c+1}º valor: '))
    if val % 2 == 0:
        l_par.append(val)
    elif val % 2 == 1:
        l_impar.append(val)
l_principal.append(l_par[:])
l_principal.append(l_impar[:])
l_principal[0].sort()
l_principal[1].sort()
print(f'Os valores pares são {l_principal[0]}')
print(f'Os valores impares são {l_principal[1]}')
'''

#-------------------- exercitando ----------------
listaprincipal = [[],[]]
for p in range(0, 7):
    num = int(input(f'Digite o {p+1}º valor: '))
    if num % 2 == 0:
        listaprincipal[0].append(num)
    else:
        listaprincipal[1].append(num)
listaprincipal[0].sort()
listaprincipal[1].sort()
print(f'Os valores pares digitados foram {listaprincipal[0]}')
print(f'Os valores impares digitados foam {listaprincipal[1]}')




















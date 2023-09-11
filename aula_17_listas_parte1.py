num = [2, 5, 9, 1]
num[2] = 3 # mudar 9 para 3
num.append(7) # acrescemtar mais uma celula com o valor 7
num.sort() # por em ordem crescente
num.sort(reverse=True) # inverter a ordem
num.insert(2, 0) # insere o valor 0 na posição 2
num.pop() #elimina o ultimo elemento
num.pop(2) #elemina o elemento na posição 2
num.remove(2)#elimina o primeiro numero 2 que ele encontrar
print(num)
print(f'essa lista tem {len(num)} elementos')

#outra forma de remover
if 4 in num:
    num.remove(4)
else:
    print('não achei o número 4')

#...............................................................................

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for v in valores:
    print(f'{v}...',end=' ')

#.................................................................................

conta = []
conta.append(5)
conta.append(6)
conta.append(2)
for z, w in enumerate(conta):
    print(f'\nNa posição {z} encontrei o valor {w}!')
print('cheguei ao final da lista')

#.................................................................................

contas = []
for c in range(0, 5):
    contas.append(input("digite um valor: "))
for k, l in enumerate(contas):
    print(f'Na posição {k} encontrei o valor {l}')
print('cheguei ao fim')

#----------------------------------------------------------------------------------------

g = [2, 3, 4, 7]
h = g[:]
h[2] = 8
print(g)
print(h)
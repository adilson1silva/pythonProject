'''teste = list()
teste.append('Adilson')
teste.append(23)
print(teste)

galera = list()
galera.append(teste[:])
teste[0] = ('Maria')
teste[1] = (40)
galera.append(teste[:])
print(galera)

#------------------------------------------------------------------------

galera1 = [['Adi', 23], ['Manuel', 45], ['Ana', 52], ['Paulo', 75]]
print(galera1)
print(galera1[0])
print(galera1[1][1])

#------------------------------------------------------------------------

galera2 = [['Adi', 23], ['Manuel', 45], ['Ana', 52], ['Paulo', 75]]
for p in galera2:
    print(p[1])
'''
#-------------------------------------------------------------------------------

galera = list()
dado = list()
totalmai = totalmen = 0
for c in range(0, 3):
    dado.append(str(input('nome: ')))
    dado.append(int(input('idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        totalmai += 1
        print(f'O {p[0]} é maior de idade.')
    else:
        totalmen += 1
        print(f'O {p[0]} é menor de idade.')
print(f'Temos {totalmai} maiores e {totalmen} menores de idade.')
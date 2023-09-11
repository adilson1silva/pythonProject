'''
tuplas são inutaveis

sorted() - escrever por ordem alfabetico
.count() - contar alguma coisa
.index() - mostrar a posição de alguma coisa
del() - apagar as tuplas da memória
'''

lanche = 'Hanburguer', 'Suco', 'Pizza', 'Pudim'

'''
print(lanche) 
print(lanche[1])
print(lanche[-2])
print(lanche[0:3])
print(lanche[0:])

lanche = 'Hanburguer', 'suco', 'lizza', 'Pudim'
for comida in lanche:
    print(f'Eu vou cumer {comida}')
print(len(lanche))
print('Comi pra caramba')

lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim'
for count in range(0, len(lanche)):
    print(count)

for count in range(0, len(lanche)):
    print(f'Hoje eu vou comer {lanche[count]}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na pasição {pos}')
print('Eu comi pra caramba!')


print(sorted(lanche))

'-----------------------------------------------------------------'

a = (2, 4, 6)
b = (8, 3, 5, 0, 6)
c = b + a
print(c.count(6))

print(c)
print(c.index(8))'''




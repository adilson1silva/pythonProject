'''

 Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato
 Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
'''
'''
lista_times = ('corintia', 'Grêmio', 'Atlético-PR', 'Cruzeiro', 'Ponte Preta', 'Nice',
               'Santos', 'Atlético', 'Avaí', 'Coritiba', 'Atlético-GO', 'Benfica', 'Porto',
               'Sporting', 'Braga', 'estoril', 'Portimão', 'Barcelona', 'Roma', 'Juventos')

print('=-'*30)
print(f'\033[1;34m Os 5 primeiros times são: {lista_times[:5]}')
print(f'\033[1;35m Os times organizado por ordem alfebetico fica: {sorted(lista_times)}')
print(f'\033[1;36m Os últimos quatro colocados são: {lista_times[15:20]}')
print(f'\033[1:37m O Avaí está na {lista_times.index("Avaí")+1} posição')




# ................................................................................................................

lista_times = ('corintia', 'Grêmio', 'Atlético-PR', 'Cruzeiro', 'Ponte Preta', 'Nice',
               'Santos', 'Atlético', 'Avaí', 'Coritiba', 'Atlético-GO', 'Benfica', 'Porto',
               'Sporting', 'Braga', 'estoril', 'Portimão', 'Barcelona', 'Roma', 'Juventos')
print(f'Os 5 primeiros times são {lista_times[0:5]}.')
print(f'Os últimos 4 colocados são {lista_times[len(lista_times)-4:len(lista_times)]}.')
print(f'os times por ordem alfabeticas são:{sorted(lista_times)}.')
print(f'A barcelona está na pisição {lista_times.index("Barcelona")+1} pasição.')

'''

#---------------------------------------------------------------------------------------------------

lista_times = ('corintia', 'Grêmio', 'Atlético-PR', 'Cruzeiro', 'Ponte Preta', 'Nice',
               'Santos', 'Atlético', 'Avaí', 'Coritiba', 'Atlético-GO', 'Benfica', 'Porto',
               'Sporting', 'Braga', 'estoril', 'Portimão', 'Barcelona', 'Roma', 'Juventos')
print(f'Os 5 primeiros times são {lista_times[:5]}')
print(f'Os últimos 4 colocados são {lista_times[len(lista_times)-4: len(lista_times)]}')
print(f'{sorted(lista_times)}')
print(f'{lista_times.index("Cruzeiro")+1}')










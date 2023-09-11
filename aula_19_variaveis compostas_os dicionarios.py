''' Dicionarios '''
'''
                    filme
   --------------------------------------------
   | 'Adilson'   | '1997'   |  'Cabo verde'   | -> print(filme.values())
   |   (values)  | (values) |  (values)       |  vai pegar o 'Adilson' '1997' 'Cabo verde'
   --------------------------------------------
   |     nome    |  D.nasc  |     País        | -> print(filme.keys())
   |    (keys)   | (keys)   |    (Keys)       | vai pegar nome, D.nasc, País
   |-------------------------------------------
   |   (Items)   |  (items) |      (items)    | print(filme.items())
   |             |          |                 | -> pega os values e os keys
   |-------------------------------------------

for k, v in filme.items():
    print(f'O (K) é (v)')

'''

pessoas = {'nome': 'Adilson', 'sexo': 'M', 'idade': 23}
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())#para mostras as chaves
print(pessoas.values())#mostrar valores
print(pessoas.items())#mostrar itens
del pessoas['sexo']# apagar algo (sexo)
pessoas['nome'] = 'daniel' # trocar o Adilson pelo Daniel
for k in pessoas.values():
    print(k)

for k, v in pessoas.items():
    print(f' {k} = {v}')

#--------------------------------------------------------------------------

# Criar dicionario dentro de uma lista

brazil  = []
estado1 = {'uf': 'Rio de Janeiro', 'siggla': 'RJ'}
estado2 = {'uf': 'são paulo', 'sigla': 'SP'}
brazil.append(estado1)
brazil.append(estado2)
print(brazil)
print(brazil[0]['uf'])

#............................................................................

cidade = dict()
brazil = list()
for c in range(0, 3):
    cidade['uf'] = str(input('unidade federativa: '))
    cidade['sigla'] = str(input('siglado estado: '))
    brazil.append(cidade.copy())
for e in brazil:
    for k, v in e.items():
        print(f'O campo {k} tem o valor {v}.')

#------------- or ----------------
for e in brazil:
    for v in e.values():
        print(v, end=' ')
print()
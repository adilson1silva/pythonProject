import moeda
p = int(input('Digite o preço R$: '))
t = float(input('Digite a taxa %: '))
print(f'O dobro do preço {moeda.moeda(p)} é de {moeda.moeda(moeda.dobro(p))}')
print(f'A metade do preço {moeda.moeda(p)} é de {moeda.moeda(moeda.metade(p))}')
print(f'Aumentando {t}%, temos {moeda.moeda(moeda.aumentar(p, t))}')
print(f'Diminuindo {t}%, temos {moeda.moeda(moeda.diminuir(p, t))}')
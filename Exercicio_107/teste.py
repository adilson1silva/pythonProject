import moeda
p = int(input('Digite o preço R$: '))
t = float(input('Digite a taxa %: '))
print(f' O dobro do preço R${p} é de R${moeda.dobro(p)}')
print(f'A metade do preço R${p} é de R${moeda.metade(p)}')
print(f'Aumentando {t}%, temos {moeda.aumentar(p, t)}')
print(f'Diminuindo {t}%, temos {moeda.diminuir(p, t)}')
from Exercicio_109 import moeda
p = int(input('Digite o preço R$: '))
t = float(input('Digite a taxa %: '))
print(f'O dobro do preço {moeda.moeda(p)} é de {moeda.dobro(p, True)}')
print(f'A metade do preço {moeda.moeda(p)} é de {moeda.metade(p, True)}')
print(f'Aumentando {t}%, temos {moeda.aumentar(p, t, True)}')
print(f'Diminuindo {t}%, temos {moeda.diminuir(p, t, True)}')
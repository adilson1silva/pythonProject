'''
Crie um programa que leia o ano de nascimento de sete pessoas. No final,
mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''
from datetime import date
count_maior = 0
count_menor = 0
idade  = 0
data_atual = date.today()
ano_atual = data_atual.year
for c in range(0, 7):
   ano_nasc = int(input('Digite o ano de nascimento: '))
   idade = ano_atual - ano_nasc
   if idade < 18:
       count_menor += 1
   else:
       count_maior += 1
print(f'Foram marcados {count_menor} pessoas com menor de 18 anos')
print(f'Doram marcados {count_maior} pessoas com maior de 18 anos')


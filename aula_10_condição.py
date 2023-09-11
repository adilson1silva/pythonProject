'''nome = str(input('Digite o seu nome: '))
if nome == 'Adilson':
    print(f'Que nome lindo você tem {nome}')
else:
    print('O seu nome é normal')
print(f'Bom dia {nome}')'''


#---------------------------------------------
 
n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'A sua média é de {m:.2f}')
if m >= 6:
    print('foi uma média boa, parabéns')
else:
    print('foi uma média má, estude mais')
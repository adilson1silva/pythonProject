'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule
 seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com
 a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
'''

peso = float(input('Digite o peso do individuo (Kg): '))
altura = float(input('Digite a altura do individuo (m): '))
IMC = peso/(altura ** 2)
if IMC < 18:
    print(f'O seu IMC é de {IMC:.2f} \033[0;31mVovê está abaixo de peso.\033[0;0m')
elif IMC >18.5 and IMC <= 25:
    print(f'O seu IMC é de {IMC:.2f} \033[0;34mO seu peso éstá bom\033[0;0m')
elif IMC >25 and IMC <= 30:
    print(f'O seu IMC é de {IMC:.2f} \033[0;35mEstás sobrepeso\033[0;0m')
elif IMC >30 and IMC <= 40:
    print(f'O seu IMC é de {IMC:.2f} \033[0;31mEsto é obesidade\033[0;0m')
else:
    print(f'O seu IMC é de {IMC:.2f} \033[0;31mEsto é obesidade Mórbida\033[0;0m')
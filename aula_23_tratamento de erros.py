'''
try:
    a = int(input('Numerador: '))
    b = int(input('Denuminador: '))
    r = a / b
except:
    print('Infelizmente tivemos um problema: ')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')

#-------------------------------------------------------------------------

try:
    a = int(input('Numerador: '))
    b = int(input('Denuminador: '))
    r = a / b
except Exception as erro:
    print(f'O problema encontrado foi {erro.__class__}: ')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')
'''
#-------------------------------------------------------------------------

try:
    a = int(input('Numerador: '))
    b = int(input('Denuminador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou. ')
except ZeroDivisionError:
    print(f'Não é possivel dividir um número por zero!')
except KeyboardInterrupt:
    print(f'O utilizador prifiriu não informar os dados.')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')
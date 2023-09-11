def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda((res))


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if formato is False else moeda((res))


def metade(preço=0, formato=False):
    res = preço / 2
    return res if formato is False else moeda(res)


def moeda(preço=0, moeda='R$', formato=False):
    return f'{moeda} {preço:8.2f}'.replace('.', ',')


def resumo(preço=0, taxaa=10, taxar=5):
    print('-'*30)
    print('RESUMO DOS PREÇOS'.center(30))
    print('-'*30)
    print(f'Preço analizado \t\t{moeda(preço)}')
    print(f'O dobro do preço é \t\t{dobro(preço,True)}')
    print(f'A metade do preço \t\t{metade(preço, True)}')
    print(f'{taxaa}% de aumento , temos \t{aumentar(preço, taxar, True)}')
    print(f'{taxar}% de redução, temos  \t{diminuir(preço, taxar, True)}')
    print('-'*30)
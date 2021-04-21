"Módulo moeda"


def aumentar(valor, taxa=0, formato=False):
    res = valor + (valor * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(valor, taxa=0, formato=False):
    res = valor - (valor * taxa/100)
    return res if formato is False else moeda(res)


def dobro(valor, formato=False):
    res = valor * 2
    return res if formato is False else moeda(res)


def metade(valor, formato=False):
    res = valor / 2
    return res if formato is False else moeda(res)


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:>8.2f}'.replace('.', ',')


def resumo(valor=0, aum=0, dim=0):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'{aum}% de aumento: \t{aumentar(valor, aum, True)}')
    print(f'{dim}% de redução: \t{diminuir(valor, dim, True)}')
    print('-' * 30)

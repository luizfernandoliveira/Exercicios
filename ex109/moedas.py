"Módulo moeda"

def aumentar(valor, formato=False):
    res = valor + (valor * 10/100)
    return res if formato is False else moeda(res)


def diminuir(valor, formato=False):
    res = valor - (valor * 13/100)
    return res if formato is False else moeda(res)

def dobro(valor, formato=False):
    res = valor * 2
    return res if not formato else moeda(res)

def metade(valor, formato=False):
    res = valor / 2
    return res if not formato else moeda(res)


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:>8.2f}'.replace('.', ',')

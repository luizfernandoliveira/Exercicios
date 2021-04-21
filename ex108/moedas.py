"Módulo moeda"

def aumentar(valor):
    return valor + (valor * 10/100)


def diminuir(valor):
    return valor - (valor * 10/100)

def dobro(valor):
    return valor * 2

def metade(valor):
    return valor / 2


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:>8.2f}'.replace('.', ',')

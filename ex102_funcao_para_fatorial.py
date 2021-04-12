'''Ex102 Função para fatorial'''


def fatorial(num, show=False):
    """
    - Função para calcular o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (Opcional) Define se irá mostrar o cálculo fatorial (True para exibir).
    :return: Retorna o resultado fatorial.
    """
    print('-' * 30)
    mult = 1
    for x in range(num, 0, -1):
        if show == True:
            print(x, end=' ')
            if x != 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        mult *= x
    return mult


# Programa principal
print(fatorial(6, True))
help(fatorial)

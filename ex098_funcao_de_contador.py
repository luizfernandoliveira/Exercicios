" Ex098 Função de contador"
from time import sleep


def contagem(inicio, fim, passo):
    sinal = 1
    print('-' * 40)
    if passo == 0:
        passo = 1
    if inicio <= fim:
        print(f'Contagem de {inicio} até {fim}, de {passo} em  {passo}.')
    else:
        if passo < 0:
            passo *= -1

        print(f'Contagem de {inicio} até {fim}, de {passo} em  {passo}.')
        sinal = -1
        passo *= -1

    for x in range(inicio, fim + sinal, passo):
        sleep(.5)
        print(x, end=' ')
    print('FIM')
    print('-' * 40)

contagem(0, 10, 1)
contagem(10, 0, 2)
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contagem(inicio, fim, passo)

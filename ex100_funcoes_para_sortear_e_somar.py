from random import randint
from time import sleep
numeros = []



def sorteia():
    print('-' * 50)
    print('Sorteando 5 valores da lista:', end=' ')
    for x in range(0, 5):
        num = randint(0, 9)
        print(num, end=' ')
        sleep(.3)
        numeros.append(num)
    print('Fim!')



def somapar():
    soma = 0
    for par in numeros:
        if par % 2 == 0:
            soma += par
    print(f'Somando os valores {numeros}, temos {soma}.')
    print('-' * 50)


sorteia()
somapar()

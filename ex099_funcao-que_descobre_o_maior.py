from random import randint
from time import sleep

# Primeira forma de fazer
'''

def maior(*num):
    print('-' * 30)
    print('Analisando os valores passados...')
    pos = 1
    maiorvalor = 0
    while pos <= vezes:
        sleep(.3)
        sor = randint(0, 9)
        print(sor, end=' ')
        if maiorvalor == 0:
            maiorvalor = sor
        if maiorvalor < sor:
            maiorvalor = sor
        pos +=1
    print()
    print(f'Foram informados {vezes} valores ao todo.')
    print(f'O maior valor é {maiorvalor}')



for x in range(0, 6):
    vezes = randint(0, 9)
    if vezes == 0:
        print('-' * 30)
        print('Não fora sorteado nenhum valor!')
    else:
        maior()
print('-' * 30)
'''

# Segunda forma de fazer

def maior(*num):
    cont = maior = 0
    print('-' * 30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior()
print('-' * 30)

"Ex106 Interactive Helping systemin python"
'''
# Primeira forma de fazer

from time import sleep


def titulo():
    sleep(0.5)
    print('\33[30;44m-' * 40)
    print(f'   Acessando o manual do comando {func}.')
    print('-' * 40)
    print('\33[m', end='')

    
while True:
    print('\33[30;42m-' * 30)
    print('Sistema de ajuda PyHELP')
    print('-' * 30)
    print('\33[m', end='')
    func = str(input('Função ou biblioteca: ')).lower()
    if func == 'fim':
        break
    sleep(0.5)
    titulo()
    print('\33[7m')
    help(func)
    print('\33[m', end='')
    sleep(0.5)
print('\33[30;41m-' * 7)
print('  FIM\33[30;41m')
print('-' * 7)
print('\33[m', end='')
'''

# Segunda forma de fazer
from time import sleep

c = ('\33[m',           # 0 - sem cores
     '\33[0;30;41m',    # 1 - vermelho
     '\33[0;30;42m',    # 2 - verde
     '\33[0;30;43m',    # 3 - amarelo
     '\33[0;30;44m',     # 4 - azul
     '\33[0;30;45m',     # 5 - roxo
     '\33[7;30m')       # 6 - branco


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


# Programa Principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYHELP', 2)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', 1)

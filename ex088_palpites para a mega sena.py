# Palpites para a mega sena

# Primeira forma de fazer
'''
from  time import sleep
from random import randint
print('-' * 30)
print('Jogo da Mega Sena')
print(f'-' * 30)
numjogos = int(input('Quantos jogos você deseja fazer? '))
contjogos = 0
print('-' * 30)
print('Sorteando')
print('-' * 30)
sleep(2)
todosjogos = []
jogo = []


while contjogos != numjogos:
    cont = 0
    while cont != 6:
        numsorteado = randint(1, 60)
        if numsorteado not in jogo:
            jogo.append(numsorteado)
            cont += 1
    todosjogos.append(jogo[:])
    jogo.clear()
    contjogos += 1
for x in range(0, numjogos):
    print(f'Jogo {x+1}: {sorted(todosjogos[x])}')
    sleep(1)
'''

# Segunda forma de fazer

from random import randint
from time import  sleep
lista = []
jogos = []
print('-' * 30)
print('JOGO DA MEGA SENA')
print('-' * 30)
quant = int(input('Quantos jogos você deseja fazer? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-' * 30, f'sorteando {quant} jogos ', '-' * 30)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-' * 30, '< Boa sorte! > ', '-' * 30)

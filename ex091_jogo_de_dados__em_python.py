# Jogo de dados em Python

# Primeira foram de fazer
'''
from random import randint
from time import sleep
jogo = {}

for x in range(1, 5):
    jogo[f'jogador{x}'] = randint(1, 6)
    print(f'jogador{x} tirou ', jogo[f'jogador{x}'], 'no dado.')
    sleep(1)
print('-' * 30)
print(F'{"RANKING DOS JOGADORES":^30}')
print('-' * 30)
c = 1
for ordem in sorted(jogo, key=jogo.get, reverse=True):
    sleep(1)
    print(f'{c}º lugar: {ordem} com {jogo[ordem]}.')
    c += 1
'''

# Segunda forma de fazer

from random import randint
from time import sleep
from operator import  itemgetter

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('-' * 30)
print(f'{"Valores sorteados":^30}')
print('-' * 30)
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-' * 30)
print('  == RANKING DE JOGADORES ==  ')
print('-' * 30)
for i, v in enumerate(ranking):
    print(f'   {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
print('-' * 30)




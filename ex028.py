# Jogo da adivinhação v.1.0

import random
from time import sleep

#Primeira forma de fazer

r = int(random.uniform(0, 6))
print('-=-'*20)
print('Vou pensar em número entre 0 e 5, tente adivinhar...')
print('-=-'*20)
n = int(input('Que o número eu pensei? '))
print('Processando...')
sleep(2)
if r == n:
    print('Você venceu!!!')
else:
    print('Você perdeu!!!')

#Segunda forma de fazer

from random import randint
from time import sleep

r = randint(0, 5)
print('-=-'*20)
print('Vou pensar em número entre 0 e 5, tente adivinhar...')
print('-=-'*20)
n = int(input('Que o número eu pensei? '))
print('Processando...')
sleep(2)
if r == n:
    print('Você venceu!!!')
else:
    print('Você perdeu!!!')

#Terceira forma de fazer
while True:
    from random import choice

    aposta = input('Adivinha qual número de 1 a 5 será escolhido: ')
    lista = [1, 2, 3, 4, 5]
    escolhido = choice(lista)

    if aposta == escolhido:
        print(f'Voce acertou o numero! {escolhido} ')
    else:
        print(f'voce errou o numero sortiado foi {escolhido}')
# Jogo da adivinhação v.1.0

import random
from time import sleep

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



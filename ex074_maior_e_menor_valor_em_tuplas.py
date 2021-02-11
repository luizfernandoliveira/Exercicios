# Maior e menor valor em tuplas

# Primeira forma de fazer
from random import randint

n = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os valores sorteados foram: {n}.')
ordem = sorted(n)
print(f'O menor número é {ordem[0]}.')
print(f'O maior número é {ordem[-1]}')

# Segunda forma de fazer
from random import randint

n = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os valores sorteados foram: ', end='')
for x in n:
    print(f'{x}', end=' ')
print(f'\nO menor número foi {min(n)}.')
print(f'O maior número foi {max(n)}')



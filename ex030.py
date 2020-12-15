# Par ou ímpar

# Primeira forma de fazer
from math import ceil, trunc

n = int(input('Digite um número qualquer: '))
nc = n/2
na = trunc(nc)
nd = nc - na
if nd == 0:
    print('O número {} é par'.format(n))
else:
    print('O número {} é ímpar'.format(n))

# Segunda maneira de fazer
n = int(input('Digite um número qualquer: '))
nd = n % 2
if nd == 0:
    print('O número {} é par'.format(n))
else:
    print('O número {} é ímpar'.format(n))

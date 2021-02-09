# Calculo fatorial

# Primeira maneira de fazer
'''
n = int(input('Digite o número para mostrar seu fatorial: '))
nfatorial = n
total = 1
while n > 0:
	total *= n
	n -= 1
print('O fatorial de {} é {}'.format(nfatorial, total))

# Segunda maneira de fazer

from math import factorial

n = int(input('Digite o número para mostrar seu fatorial:'))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))
'''
# Terceira forma de fazer

n = int(input('Digite o número para mostrar seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end= ' ' )
while c > 0:
	print('{}'.format(c), end=' ' )
	print(' x ' if c > 1 else ' = ' , end=' ')
	f  *= c
	c -= 1
print(f)


	
	
# Número primo

n  = int(input('Digite um número: '))
cont = 0
for x in range(1, n + 1):
	t = n  %  x
	div = 0
	if t == 0:
		div += 1
		print('\033[32m{}\033[m'.format(x), end=' ')
		cont += 1
	else:
		print('\033[31m{}\033[m'.format(x), end=' ')
if cont == 2:
	print('\033[34m{} é um número primo.\033[m'.format(n))
else:
	print('\033[34m{} não é um número primo.\033[m'.format(n))
	
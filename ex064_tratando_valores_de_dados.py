# Tratando varios valores

# Primeira forma de fazer

cont = 0 
soma = 0
n = 1
while n != 999:
	n = int(input('Digite um número: '))
	if n == 999:
		print('Finalizando...')
	else:
		soma += n
		cont += 1
print('A quantidade de números digitados foi {} e a soma foi {}.'.format(cont, soma))

# Segunda forma de fazer

cont = soma = 0
n = int(input('Digite um número: '))
while n != 999:
	soma += n
	cont += 1
	n = int(input('Digite um número: '))
print('A quantidade de números digitados foi {} e a soma foi {}.'.format(cont, soma))

# Sequência de Fibonacci

# Primeira forma de fazer

print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)

termos = int(input('Quantos termos da sequência de Fibonacci você deseja? '))
atual = 1
cont = 0
anterior = 0
fib = 0
print('0 -> 1 -> ', end = '')
while  cont < termos:
	if cont == 0:
		atual == 1
		fib = atual + anterior
		print(fib, end= ' -> ')
		anterior = atual
		cont += 3
	else:
		atual = fib
		fib = atual + anterior
		print(fib, end= ' -> ')
		anterior = atual
		cont += 1		
	
print('Fim')

# Segunda forma de fazer

print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)

n = int(input('Quantos termos da sequência de Fibonacci você deseja? '))
t1 = 0
t2 = 1
print('{} -> {} -> '.format(t1, t2), end ='')
cont = 3 
while cont <= n:
	t3 = t1 + t2
	print(t3, end=' -> ')
	t1 = t2
	t2 = t3
	cont += 1
print('Fim')


# Mostre o maior número e o menor

#Primeira forma de fazer

n1 =  int(input('Digite o primeiro número: '))
n2 =  int(input('Digite o segundo número: '))
n3 =  int(input('Digite o terceiro número: '))

if n1 > n2 > n3:
	print('O número {} é o maior número'.format(n1))
	print('O número {} é o menor número'.format(n3))
elif n2>n3>n1:
	print('O número {} é o maior número'.format(n2))
	print('O número {} é o menor número'.format(n1))
elif n3>n1>n2:
	print('O número {} é o maior número'.format(n3))
	print('O número {} é o menor número'.format(n2))
elif  n1>n3>n2:
	print('O número {} é o maior número'.format(n1))
	print('O número {} é o menor número'.format(n2))
elif n3>n2>n1:
	print('O número {} é o maior número'.format(n3))
	print('O número {} é o menor número'.format(n1))
elif n2>n1>n3:
	print('O número {} é o maior número'.format(n2))
	print('O número {} é o menor número'.format(n3))

# Segunda forma de fazer

n1 =  int(input('Digite o primeiro número: '))
n2 =  int(input('Digite o segundo número: '))
n3 =  int(input('Digite o terceiro número: '))

maior = n1
if n2 > n1 and n2 > n3:
	maior = n2
if n3 > n1 and n3 > n2:
	maior = n3

menor = n1
if n2 < n1 and n2 < n3:
	menor = n2
if n3 < n1 and n3 < n2:
	menor = n3
print('O número {} é o maior número'.format(maior))
print('O número {} é o menor número'.format(menor))



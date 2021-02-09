# Progressão aritmética

#Primeira forma de fazer
pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))

d = pt
for x in range(1, 11):
	print(d, end=' -> ')
	d += r
print('FIM')

#Segunda forma de fazer
t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
decimo = pt + (10 - 1) * r
for x in range(pt, decimo + r, r):
	print('{}'.format(x), end=' -> ')
print('Fim')
	
	
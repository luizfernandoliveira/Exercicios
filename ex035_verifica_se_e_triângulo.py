# Determine se as medidas formam um triângulo.

a = float(input('Digite o primeiro lado do triângulo: '))
b = float(input('Digite o ssegundo lado do triângulo: '))
c = float(input('Digite o terceiro lado do triângulo: '))

if a + b > c and b + c > a and c + a > b:
	print('Os números {}, {} e {} podem formar um triângulo!'.format(a, b, c))
else:
	print('Os números {}, {} e {} não podem formar um triângulo!'.format(a, b, c))
	
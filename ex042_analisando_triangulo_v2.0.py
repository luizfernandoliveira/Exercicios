# Determine se as medidas formam um triânguloe e qual tipo dw triângulo é formado.

a = float(input('Digite o primeiro lado do triângulo: '))
b = float(input('Digite o ssegundo lado do triângulo: '))
c = float(input('Digite o terceiro lado do triângulo: '))

if a + b > c and b + c > a and c + a > b:
	print('Os números {}, {} e {} podem formar um triângulo!'.format(a, b, c))
	if a == b == c:
		print('O triângulo é EQUILÁTERO.')
	elif a == b != c or a!= b == c:
		print('O triângulo é ISÓSCELES.')
	else:
		print('O triângulo é ESCALENO.1b')
else:
	print('Os números {}, {} e {} não podem formar um triângulo!'.format(a, b, c))
	
# Tabuada v3.0
while True:
	n = int(input('Qual tabuada deseja: '))
	if n < 0:
		break
	c = 0
	while c <= 10:
		print(f'{n} X {c:2} = {n * c:2}')
		c += 1
print(f'Programa de tabuada encerrado!')
		

	
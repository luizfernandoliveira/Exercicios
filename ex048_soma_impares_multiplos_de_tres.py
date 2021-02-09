# Soma impares multiplo de três
			
x = 0
total = 0
c = 0

for x in range(1, 500):
	if x % 2 != 0 and x % 3 == 0:
		total += x
		c += 1
print('O total dos números ímpares e divisíveis por 3 é {}. Contendo {} números que se enquadram nestas condições.'.format(total, c))

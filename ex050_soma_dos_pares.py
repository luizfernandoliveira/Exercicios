#Soma dos pares

t = 0
c = 0
for x in range(1, 7):
	n = int(input('Digite o número inteiro {}: '.format(x)))
	if n % 2 == 0:
		t += n
		c += 1
print('Você digitou {} números PARES. A soma dos números pares é {}'.format(c, t))
	
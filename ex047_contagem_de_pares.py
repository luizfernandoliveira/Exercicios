# Todos os números pares de 0 a 50

# Primeira maneira de fazer
for x in range(0, 51):
	if x % 2 == 0:
		print(x)
print('fim')
		
# Segunda maneira de fazer
for x in range(0, 51, 2):
	print(x, end=' ')

print('fim')

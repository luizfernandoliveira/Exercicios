# Varios numeros com flag
soma = cont = 0
while True:
	n = int(input('Digite um número: '))
	if n == 999:
		break
	cont += 1
	soma += n
print(f'Você digitou {cont} números e soma deles é {soma}.')
	

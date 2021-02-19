# Maior e menor valor na lista


# Primeira forma de fazer:
	
lista = []
cont = 0

while cont != 5:
	n = int(input('Digite o valor {}: '.format(cont)))
	lista.append(n)
	cont += 1
print(lista)
max = max(lista)
print(f'O valor máximo da lista é {max} e está na posição ', end='')
for c, v in enumerate(lista):
	if v == max:
		print(f'{c}', end='...')
min = min(lista)
print(f'\nO valor mínimo da lista é {min} e está na posição ')
for c, v in enumerate(lista):
	if v == min:
		print(f'{c}', end='...')
print('\nFim')
		
# Segunda forma de fazer

min = max = 0
lista = []
for c in range(0, 5):
	lista.append(int(input(f'Digite o valor da posição {c}: ')))
	if c == 0:
		min = max = lista[c]
	else:
		if max < lista[c]:
			max = lista[c]
		if min > lista[c]:
			min = lista[c]
print(f'Você digitou os valores: {lista}')
print(f'O valor máximo da lista é {max} e está na posição ', end='')
for c, v in enumerate(lista):
	if v == max:
		print(f'{c}', end='...')
print(f'\nO valor mínimo da lista é {min} e está na posição ')
for c, v in enumerate(lista):
	if v == min:
		print(f'{c}', end='...')
print('\nFim')
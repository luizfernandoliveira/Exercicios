# Mais sobre matriz

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0,3):
	for c in range(0, 3):
		matriz[l][c] = int(input(f'Digite um valor para [ {l}, {c} ]: '))
print('-' * 30)
for l in range(0, 3):
	for c in range(0, 3):
		print(f'[{matriz[l][c]:^5}]', end=' ')
	print()
print('-' * 30)
somapar = maiorlinha2 = soma3coluna = 0
for l in range(0, 3):
	for c in range(0, 3):
		if matriz[l][c] % 2 == 0:
			somapar += matriz[l][c]
print(f'A soma dos pares é {somapar}.')
for l in range(0, 3):
	soma3coluna += matriz[l][2]
print(f'A soma da terceira coluna é {soma3coluna}.')
for l2 in matriz[1]:
	if maiorlinha2 == 0:
		maiorlinha2 = l2
	elif maiorlinha2 < l2:
		maiorlinha2 = l2
print(f'O maior valor da linha 2 é {maiorlinha2}.')

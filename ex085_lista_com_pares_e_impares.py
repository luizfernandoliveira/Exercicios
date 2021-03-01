# Lista com pares e ímpares

lista = [ [], [] ]
for x in range(0,7):
	a = int(input('digite: '))
	if a % 2 ==0: 
		lista[0].append(a)
	else:
		lista[1].append(a)
print(f'Os  números pares digitados foram {sorted(lista[0])}.')
print(f'Os números ímpares digitados fomram {sorted(lista[1])}.')

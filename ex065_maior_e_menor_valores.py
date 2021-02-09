# Maior e menor valores

# Primeira forma de fazer

cont = 0
soma = 0
opcao = 'S'
n = 0
maior = n
menor = n
while opcao != 'N':
	n = int(input('Digite um número: '))
	soma += n
	cont += 1
	if menor == 0:
		menor = n
	if maior < n:
		maior = n
	if menor > n:
		menor = n
	opcao = str(input('Deseja digitar outro número? (S/N). ')).strip().upper()
media = soma / cont
print('Você digitou {}. A média dos valores digitados é {}.'.format(cont, media))
print('O maior número digitado foi {}.'.format(maior))
print('O menor número digitado foi {}.'.format(menor))

# Segunda forma de fazer

resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
	num = int(input('Digite um número: '))
	soma += num
	quant += 1 
	if quant == 1:
		maior = menor = num
	else:
		if num > maior:
	 		maior = num
		if num < menor:
			menor = num
	resp =  str(input('Deseja digitar outro número? ( S/N) '))
media = soma / quant
print('Você digitou {}. A média dos valores digitados é {}.'.format(quant, media))
print('O maior número digitado foi {}.'.format(maior))
print('O menor número digitado foi {}.'.format(menor))

 
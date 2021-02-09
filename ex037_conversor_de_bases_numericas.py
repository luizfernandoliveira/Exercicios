# conversor de bases númericas

# Primeira forma de fazer

conversao = []
b = int(input('Digite um número: '))
print('Escolha uma opcão abaixo: ')
print('(1) Binário')
print('(2) Octal')
print('(3) Hexadecimal')
opcao = int(input('Digite a opção: '))
if opcao == 1:
	print('Binário foi a opção escolhida!')	
	while b >= 2:
		conversao.append(b % 2)
		b = b // 2
	conversao.append(1)
	conversao.reverse()
	print('O número binário é ', *conversao)
	b

elif opcao == 2:
	print('Octal foi a opção escolhida!')	
	while b >= 8:
		conversao.append(b % 8)
		b = b // 8
	conversao.append(b)
	conversao.reverse()
	print('O número octal é ', *conversao)
elif opcao ==3:
	print('Hexadecimal foi a opção escolhida!')	
	while b >= 16:
		br = b % 16
		if br == 10:
			br = 'A'
		elif br == 11:
			br = 'B'
		elif br == 12:
			br = 'C'
		elif br == 13:
			br = 'D'
		elif br == 14:
			br = 'E'
		elif br == 15:
			br = 'F'
		conversao.append(br)
		b = b // 16
	if b == 10:
		b = 'A'
	elif b == 11:
		b = 'B'
	elif b == 12:
		b = 'C'
	elif b == 13:
		b = 'D'
	elif b == 14:
		b = 'E'
	elif b == 15:
		b = 'F'
	conversao.append(b)
	conversao.reverse()
	print('O número hexadecimal é ', *conversao)

# Segunda forma de fazer

b = int(input('Digite um número: '))
print('Escolha uma opcão abaixo: ')
print('(1) Binário')
print('(2) Octal')
print('(3) Hexadecimal')
opcao = int(input('Digite a opção: '))
if opcao == 1:
	print('Binário foi a opção escolhida!')
	print(bin(b))
elif opcao == 2:
	print('Octal foi a opção escolhida!')
	print(oct(b))
elif opcao ==3:
	print('Hexadecimal foi a opção escolhida!')	
	print(hex(b))



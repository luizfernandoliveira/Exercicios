# Validação de dados
s = str(input('Digite o sexo (M ou F): ')).strip().upper() [0]
print(s)
while s not in 'FM':
	s = str(input('Valor inválido! Digite o sexo novamente: ')).strip().upper() [0]
	print(s)
print('Você digitou o sexo {}.'.format(s))

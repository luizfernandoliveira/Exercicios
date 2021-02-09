# Progressao aritmétiva v3.0

# Primeira maneira de fazer
'''
pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 1
c2 = 0
t = pt
opcao = 1
termos = 10

while opcao != 0:
	c =1
	while  c <= termos:
		print(t, end=' -> ')
		t += r
		c += 1
		c2 += 1
	print('Pausa')
	opcao = int(input('Deseja exibir quantos termos a mais? '))
	if opcao != 0:
		termos = opcao
else:
	print('Progressão finalizada com {} termos para o número {} como o primeiro termo e com razão de {}.'.format(c2, pt, r))
	'''
# Segunda maneira de fazer

pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 0
t = pt
total = 0
mais = 10
while  mais != 0:
	total = total + mais
	while  c <= total:
		print(t, end=' -> ')
		t += r
		c += 1
	print('Pausa')
	mais = int(input('Deseja exibir quantos termos a mais? '))
print('Progressão finalizada com {} termos para o número {} como o primeiro termo e com razão de {}.'.format(total, pt, r))

	
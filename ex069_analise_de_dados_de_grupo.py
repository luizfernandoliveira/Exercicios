# Analise de dados de grupo

m18 = h = m20 = 0
while True:
	print('-' * 30)
	print('Cadastro de pessoas')
	print('-' * 30)
	idade = int(input('Idade: '))
	sexo = ' '
	while sexo not in 'MF':
		sexo = str(input('Sexo (f/m): ')).strip().upper()
	if idade >= 18:
		m18 += 1
	if sexo ==  'M':
		h += 1 
	if idade  < 20 and sexo == 'F':
		m20 += 1
	opcao = ' '
	while opcao not in 'SN':
		opcao = str(input('Deseja cadastrar outra pessoa? (s / n) ')).strip().upper()
	if opcao in 'Nn':
		break
print("-" * 30)
print(f'Foram cadastrados {m18} pessoas maiores de 18 anos.')
print(f'Foram cadastrados {h} homens.')
print(f'Foram cadastradas {m20} mulheres com menos de 20 anos.')
		
	
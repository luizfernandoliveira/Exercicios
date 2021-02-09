# Analisador completo

soma_idade = 0
media_idade = 0
maior_idade = 0
nome_maior = ''
feminino_menor = 0
for x in range(1, 5):
	print('------ PESSOA {} ------'.format(x))
	nome = str(input('Nome: ')).strip()
	idade = int(input('Idade: '))
	sexo = str(input('Sexo (digite M ou F): ')).strip()
	soma_idade += idade
	if x == 1 and sexo in 'Mm':
	 	maior_idade = idade
	else:
	 	 if idade > maior_idade and sexo in 'Mm':
	 	 	maior_idade = idade
	 	 	nome_maior = nome
	if sexo in 'Ff' and idade < 20:
		feminino_menor  += 1
	 
media_idade = soma_idade / 4
print('A média de idade é {} anos.'.format(media_idade)) 
print('O homem com maior idade é {} e possui {} anos.'.format(nome_maior, maior_idade))
if feminino_menor == 0:
	print('Não possui mulheres abaixo de 20 anos.')
elif feminino_menor == 1:
	print('Possui {} mulher abaixo de 20 anos.'.format(feminino_menor))
else:
	print('Possui {} mulheres abaixo de 20 anos.'.format(feminino_menor))

	 
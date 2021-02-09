# Grupo de maioridade
from datetime import date

cont_maior = 0
cont_menor = 0
data_atual = date.today().year
for x in range(1, 8):
	a = int(input('Digite a data de nascimento da {} pessoa: '.format(x)))
	if (data_atual - a) >= 21:
		cont_maior += 1
	else:
		cont_menor += 1
print('O total de pessoas maiores de idade é {}.'.format(cont_maior))
print('O total de pessoas menores de idafe é {}.'.format(cont_menor))
		
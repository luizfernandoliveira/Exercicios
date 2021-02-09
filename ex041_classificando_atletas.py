# Classificando atletas

from datetime import date

an = int(input('Digite o ano de nascimento do atleta: '))
data_atual = date.today().year
idade = data_atual - an

print('A idade atual do atleta é {} anos.'.format(idade))
if idade <= 9:
	print('Classificação: MIRIM.')
elif idade <= 14:
	print('Classificação: INFANTIL.')
elif idade <= 19:
	print('Classificação: JÚNIOR.')
elif idade <=  25:
	print('Classificação:  SÊNIOR.')
elif idade > 25:
	print('Classificação: MASTER.')
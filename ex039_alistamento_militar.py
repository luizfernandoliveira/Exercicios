 # Alistamento militar
 
from datetime import date
 
ano = int(input('Digite o ano que você nasceu: '))
data_atual = date.today().year
idade = data_atual - ano
tempo_alistar  = 18 - idade
tempo_ultrapassado = idade - 18
print('No ano atual, {}, Você tem {} anos!'.format(data_atual, idade ))
if idade == 18:
	print('Você precisa se alistar este ano!')
elif idade < 18:
	print('Você precisará se alistar daqui a {} anos.'.format(tempo_alistar))
else:
	print('Você deveria ter se alistado a {} anos.'.format(tempo_ultrapassado))

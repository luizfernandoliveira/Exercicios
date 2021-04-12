"EX101 Funções para votação"

# Primeira forma de fazer
'''
from datetime import date

def voto(resp=1):
	if 18 <= idade <= 65:
		return 'VOTO OBRIGATÓRIO'
	elif idade < 16:
		return 'NÃO VOTA'
	else:
		return 'VOTO OPCIONAL'
	

ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
resp = voto(idade)
print(f'Com {idade} anos: {resp}. ')
'''

# Segunda forma de fazer

def voto(ano):
	from datetime import date
	atual = date.today().year 
	idade = atual - ano
	if idade < 16:
		return f'Com {idade} anos: NÃO VOTA.'
	elif 16 <= idade < 18 or idade > 65:
		return f'Com {idade} anos: VOTO OPCIONAL.'
	else:
		return f'Com {idade} anos: VOTO OBRIGATÓRIO'
		

nasc  = int(input('Digite o ano de nascimento: '))
print(voto(nasc))

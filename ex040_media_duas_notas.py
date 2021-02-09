# Média entre duas notas

n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
m = (n1 + n2)/2
print('A sua média foi {:.2f}'.format(m))
if m < 5:	
	print('Você foi reprovado!')
elif 5 <= m < 7:
	print('Você está de exame!')
elif m >= 7:
	print('Você foi aprovado!')
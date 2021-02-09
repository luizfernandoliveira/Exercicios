# Aprovando empréstimo

casa = float(input('Qual o valor da casa: R$'))
salario = float(input('Qual o salário: R$'))
tempo = float(input('Em quantos anos será pago: '))
parcela = casa / (tempo * 12)

if parcela > (salario*(30/100)):
	print('O empréstimo negado!')
else:
	print('Empréstimo aprovado!')
print('O valor da parcela será R${:.2f}. O valor máximo para sua parcela é de R${:.2f}.'.format(parcela, (salario*(30/100))))


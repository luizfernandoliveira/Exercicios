# Gerenciador de pagamentos

print('{:=^40}'.format(' LOJA '))

produto = float(input('Digite o preço do produto: '))
print('Qual a forma de pagamento?')
print('(1) Á vista dinheiro/ cheque')
print('(2) Á vista cartão de crédito')
print('(3) 2 x no cartão')
print('(4) 3 x ou mais no cartão')
opcao = int(input('Digite a opção de pagamento: '))

if opcao == 1:
	preco = produto - ((produto * 10)/100)	
elif opcao == 2:
	preco = produto - ((produto * 5)/100)
	print('Opção escolhida: Á vista dinheiro/ cheque')
elif opcao == 3:
	preco = produto
elif opcao == 4:
	preco = produto + ((produto * 20)/100)
	qparcelas = int(input('Quantas parcelas? R$'))
	print('A compra será parcelada em {}x e cada parcela será R${:.2f}'.format(qparcelas, preco/qparcelas))
else:
		print('Opção inválida.')
		preco = produto
print('O preço do produto é R${:.2f}.'.format(preco))
	
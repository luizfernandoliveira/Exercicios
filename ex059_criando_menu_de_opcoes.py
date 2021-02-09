# Criando um menu de opções

def separador():
	print('-'*30)
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

opcao = 0
while opcao != 5:
	print(
 		'''
 	(1) Somar
 	(2) Multiplicar
 	(3) Maior
 	(4) Novos números
 	(5) Sair do programa
 		''')
	separador()
	opcao = int(input('Digite a opção desejada: '))
	if opcao == 1:
		print('A soma entre {} e {} é {}.'.format(n1, n2, n1 + n2))
		separador()
	elif opcao == 2:
		print('A multiplicação  entre {} e {} é {}.'.format(n1, n2, n1 * n2))
		separador()
	elif opcao == 3:
		if n1 > n2:
			print('O número {} é maior.'.format(n1))
			separador
		else:
			print('O número {} é maior.'.format(n2))
			separador()
	elif opcao == 4:
		n1 = int(input('Digite o primeiro valor: '))
		n2 = int(input('Digite o segundo valor: '))
	elif opcao != 1 or opcao !=2 or opcao !=3 or opcao !=4 or opcao !=5:
		print('Opção inválida!')
		separador()

print('Finalizando programa...\nFinalizado!')

	
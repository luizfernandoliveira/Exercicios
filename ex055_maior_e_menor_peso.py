#  maior e menor peso

# Primeira foema de fazer
lista = []
for x in range(1, 6 ):
	p = float(input('Digite o peso da pessoa {} (em Kg): '.format(x)))
	lista.append(p)
lista_ordem = sorted(lista)
contagem_lista = len(lista)
print('O menor peso é {:.2f} Kg.'.format(lista_ordem[0]))
print('O maior peso é {:.2f} Kg.'.format(lista_ordem[contagem_lista - 1]))

# Segunda forma de fazer
maior = 0
menor = 0
for x in range(1, 6):
	p = float(input('Digite o peso da pessoa {} (em Kg): '.format(x)))
	if x == 1:
		maior = p
		menor = p
	else:
		if p > maior:
			maior = p
		if p < menor:
			menor = p
print('O maior peso é {:.2f} Kg.'.format(maior))
print('O menor peso é {:.2f} Kg.'.format(menor))
	
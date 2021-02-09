# Detector de palindromo

t = str(input('Digite o texto: ')).strip().upper()
lista = t.split()
juntar = '' .join(lista)
inv = ''
for letra in range(len(juntar) - 1, -1 , -1):
	inv += juntar[letra]
print('O inverso de {} é {}.'.format(juntar, inv))
if juntar == inv:
	print('O texto {} é um palíndromo!'.format(t))
else: 
	print('O texto {} não é um palíndromo!'.format(t))

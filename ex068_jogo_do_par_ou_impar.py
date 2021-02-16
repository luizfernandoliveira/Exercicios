# Jogo do par ou impar

from random import randint
print('=' * 30)
print('Jogo do par ou impar')
print('=' * 30)
tentativas = 0
while True:
	print('-' * 30)
	c = randint(0, 10)
	n = int(input('Digite um número: '))
	opcao  = str(input('Digite par ou impar(p/i): ')).strip().upper()
	soma = c + n
	res = soma % 2
	if res == 0:
		np = 'P'
		valor = 'par'
	else:
		np = 'I'
		valor = 'ímpar'
	if opcao == np:
		print(f'Você venceu! O computador escolheu {c} e você {n} a soma deu {soma} e este número é {valor}. Vamos jogar novamente...')
		tentativas +=1
	else:
		print(f'Você perdeu! O computador escolheu {c} e você {n} e a soma deu {soma} e este número é {valor}.')
		break
print(f'Fim de jogo. Você venceu {tentativas} vezes!')

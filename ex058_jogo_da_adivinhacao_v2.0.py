# Jogo da adivinhação V2.0

# Primeira forma de fazer
'''
from random import randint
from time import sleep

escolhido = randint(0, 10)
print('-=-'*20)
print('Vou pensar em número entre 0 e 10, tente adivinhar...')
print('-=-'*20)
escolha = int(input('Que o número eu pensei? '))
cont = 1
while escolhido != escolha:
	print('Processando...')
	sleep(2)
	print('Você perdeu! Tente novamente!')
	escolha = int(input('Qual o número eu pensei? '))
	cont += 1
print('Você acertou após {} tentativas.'.format(cont))
'''

# Segunda forma de fazer

from random import randint
from time import sleep

escolhido = randint(0, 10)
print('-=-'*20)
print('Vou pensar em número entre 0 e 10, tente adivinhar...')
print('-=-'*20)
escolha = int(input('Que o número eu pensei? '))
cont = 1
while escolhido != escolha:
	print('Processando...')
	sleep(2)
	cont += 1
	if escolha < escolhido:
		print('Mais...')
	else:
		print('Menos...')
	print('Você perdeu! Tente novamente!')
	escolha = int(input('Qual o número eu pensei? '))
print('Você acertou após {} tentativas.'.format(cont))

# Terceira forma de fazer

from random import randint

computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False 
palpites = 0
while not acertou:
	jogador = int(input('Qual é o seu palpite?'))
	palpites += 1
	if jogador == computador:
		acertou = True
	else:
		if jogador < computador:
			print('Mais... Tente outra vez!')
		else:
			print('Menos... Tente outra vez!')
print('Você acertou com {} tentativas!'.format(palpites))

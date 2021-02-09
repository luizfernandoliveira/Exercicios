# Game: Jokempô (pedra, papel e tesouro)

#Primeira forma de fazer
'''
import random
from time import sleep

jokenpo = [1, 2, 3]

def separador():
	return print('-' * 40)

def separador1():
	return print('=' * 40)
	
def temporizador():
	print('JO')
	sleep(1)
	print('KEN')
	sleep(1)
	print('PÔ')
	sleep(1)

while True:
	separador1()
 
	escolha = int(input('Qual a sua jogada? '))
		
	pc = random.choice(jokenpo)
	if pc == 1 and escolha == 1:
		separador()
		temporizador()
		print('A escolha do computador foi Pedra')
		print('Sua escolha foi Pedra')
		separador()
		print('EMPATE!')
		print('Pedra empata com Pedra!')
		
	elif pc == 2 and escolha == 1:
		separador()
		temporizador()
		print('A escolha do computador foi Papel')
		print('Sua escolha foi Pedra')
		separador()
		print('Você Perdeu!')
		print('Papel vence pedra!')
	elif pc == 3 and escolha == 1:
		separador()
		temporizador()
		print('A escolha do computador foi Tesoura')
		print('Sua escolha foi Pedra')
		separador()
		print('Você Venceu!')
		print('Pedra vence tesoura!')
	elif pc == 1 and escolha == 2:
		separador()
		temporizador()
		print('A escolha do computador foi Pedra')
		print('Sua escolha foi Papel')
		separador()
		print('Você Venceu!')
		print('Papel vence Pedra!')
	elif pc == 2 and escolha == 2:
		separador()
		temporizador()
		print('A escolha do computador foi Papel')
		print('Sua escolha foi Papel')
		separador()
		print('EMPATE!')
		print('Papel empata com Papel!')
	elif pc == 3 and escolha == 2:
		separador()
		temporizador()
		print('A escolha do computador foi Tesoura')
		print('Sua escolha foi Papel!')
		separador()
		print('Você Perdeu!')
		print('Tesoura vence  Papel!')
	elif pc == 1 and escolha == 3:
		separador()
		temporizador()
		print('A escolha do computador foi Pedra')
		print('Sua escolha foi Tesoura!')
		separador()
		print('Você Perdeu!')
		print('Pedra vence Tesoura!')
	elif pc == 2 and escolha == 3:
		separador()
		temporizador()
		print('A escolha do computador foi Papel')
		print('Sua escolha foi Tesoura')
		separador()
		print('Você Venceu!')
		print('Tesoura vence Papel! ')
	elif pc == 3 and escolha == 3:
		separador()
		temporizador()
		print('A escolha do computador foi Tesoura!')
		print('Sua escolha foi Tesoura!')
		separador()
		print('EMPATE!')
		print('Tesoura empata com Papel!')
	separador1()
	print('')
	'''
#Segunda forma de fazer

from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print("""Opções:
(0) Pedra
(1) Papel
(2) Tesouro
	""")
	
escolha = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('-' * 40)
print('A escolha do computador foi {}'.format(itens[computador]))
print('Sua escolha foi {}'.format(itens[escolha]))
print('-' * 40)


if computador == 0:
	if escolha == 0:
		print('EMPATE!')
	elif escolha == 1:
		print('Você VENCEU!')
	elif escolha == 2:
		print('Você PERDEU!')
	else:
		print('Jogada inválida!')

elif computador == 1:
	if escolha == 0:
		print('Você PERDEU!')
	elif escolha == 1:
		print('EMPATE!')
	elif escolha == 2:
		print('Você VENCEU!')
	else:
		print('Jogada inválida!')

elif computador == 2:
	if escolha == 0:
		print('Você VENCEU!')
	elif escolha == 1:
		print('Você PERDEU!')
	elif escolha == 2:
		print('empate!')
	else:
		print('Jogada inválida!')



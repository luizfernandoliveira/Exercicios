#Analisador de textos

#Primeira forma de fazer
nome = input('Digite seu nome completo: ')
print('O nome em maíusculo é {}'.format(nome.upper()))
print('O nome em minúsculo é {}.'.format(nome.lower()))
contagem = nome.count(' ')
caracter = len(nome)
caracter_sem_espaco = caracter - contagem
print('Seu nome ao todo tem {} letras.'.format(caracter_sem_espaco))
div = nome.split()
print('O primeiro nome possui {} letras.'.format(len(div[0])))

#Segunda maneira de fazer
nome = str(input('Digite seu nome completo: ')).strip()
print('O nome em maíusculo é {}'.format(nome.upper()))
print('O nome em minúsculo é {}.'.format(nome.lower()))
print('Seu nome ao todo tem {} letras.'.format(len(nome) - nome.count(' ')))
print('O primeiro nome possui {} letras.'.format(nome.find(' ')))

#Terceira maneira de fazer
nome = str(input('Digite seu nome completo: ')).strip()
print('O nome em maíusculo é {}'.format(nome.upper()))
print('O nome em minúsculo é {}.'.format(nome.lower()))
print('Seu nome ao todo tem {} letras.'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('O primeiro nome possui {} letras.'.format(len(separa[0])))

#Primeiro e último nome de uma pessoa

#Primeira forma de fazer
nome = str(input('Digite seu nome completo: ')).strip()
nome_div = nome.split()
contagem = len(nome_div)
print('O primeiro nome é {}.'.format(nome_div[0]))
print('O último nome é {}.'.format(nome_div[contagem-1]))

#Segunda forma de fazer
nome = str(input('Digite seu nome completo: ')).strip()
nome_div = nome.split()
print('O primeiro nome é {}.'.format(nome_div[0]))
print('O último nome é {}.'.format(nome_div[len(nome_div)-1]))

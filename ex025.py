#Procurando string dentro de outra

#Primeira forma de fazer
nome = str(input('Digite seu nome completo: ')).strip()
nome_maiusculo = nome.upper()
print('SILVA' in nome_maiusculo)

#Segunda forma de fazer
nome = str(input('Digite seu nome completo: ')).strip()
print('Possui SILVA no seu nome? {}'.format('SILVA' in nome.upper()))


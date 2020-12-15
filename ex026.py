#Primeira e última ocorrência em uma string

#Primeira forma de fazer
frase = str(input('Digite uma frase: ')).strip()
frase_maiuscula = frase.upper()
contagem = frase_maiuscula.count('A')
print('Contém {} letras A na frase.'.format(contagem))
print('A letra A aparece a primeira vez na posição {}.'.format(frase_maiuscula.find('A')))
print('A última letra A aparece na posição {}.'.format(frase_maiuscula.rfind('A')))

#Segunda forma de fazer
frase = str(input('Digite uma frase: ')).upper()
print('Contém {} letras A na frase.'.format(frase.count('A')))
print('A letra A aparece a primeira vez na posição {}.'.format(frase.find('A')))
print('A última letra A aparece na posição {}.'.format(frase.rfind('A')))
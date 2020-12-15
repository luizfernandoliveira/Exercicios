#verificando as primeiras letras de um texto

#Primeira forma e fazer
cidade = str(input('Em que cidade você nasceu? '))
cidade_maiuscula = cidade.upper()
cidade_div = cidade_maiuscula.strip().split()
print('SANTO' in cidade_div[0])

#Segunda maneira de fazer
cidade = str(input('Em que cidade você nasceu? ')).strip()
print((cidade[:5].upper()) == 'SANTO')

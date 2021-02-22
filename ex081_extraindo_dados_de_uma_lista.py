# Extraindo dados de uma lista

lista = []

while True:
    a = (int(input('Digite um valor: ')))
    if a not in lista:
        lista.append(a)
        print('Valor adicionado com sucesso!')
    else:
        print(f'Valor duplicado! o valor {a} já foi digitado.')
    opcao = ' '
    while opcao not in 'NS':
        opcao = str(input('Deseja digitar outro número? (s / n) ')).strip().upper()
    if opcao in 'Nn':
        break
print('-' * 30)
print(f'Foram digitados {len(lista)} números.')
lista.sort(reverse=True)
print(f'A lista de forma decrescente é {lista}.')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
print('Fim')

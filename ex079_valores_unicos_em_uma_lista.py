# Valores únicos em uma lista

lista = []

igual = 0
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
lista.sort()
print(f'Você digitou os valores {lista}')
print('Fim')

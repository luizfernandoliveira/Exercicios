# Dividindo valores em várias listas

# Primeira forma de fazer

# lista= []
# pares = []
# impares = []
#
# while True:
#     a = (int(input('Digite um valor: ')))
#     lista.append(a)
#     print('Valor adicionado com sucesso!')
#     opcao = ' '
#     while opcao not in 'NS':
#         opcao = str(input('Deseja digitar outro número? (s / n) ')).strip().upper()
#     if opcao in 'Nn':
#         break
# print('-' * 30)
# print(f'a lista completa é {lista}.')
# for c in lista:
#     if c % 2 == 0:
#         pares.append(c)
#     else:
#         impares.append(c)
# if len(pares) == 0:
#     print('A lista de pares está vazia.')
# else:
#     print(f'A lista de pares é {pares}.')
# if len(impares) == 0:
#     print('A lista de impares está vazia.')
# else:
#     print(f'A lista de ímpares é {impares}.')

# Segunda forma de fazer

num = []
pares = []
impares = []
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? (S/N)'))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-' * 30)
print(f'A lista completa é {num}.')
print(f'A lista de pares é {pares}.')
print(f'A lista de ímpares é {impares}.')

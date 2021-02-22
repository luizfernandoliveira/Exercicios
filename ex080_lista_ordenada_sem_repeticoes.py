# Lista ordenada sem repetições

# Primeira forma de fazer
#
# lista = []
# valores = 0
#
# while valores != 5:
#     a = (int(input('Digite um valor: ')))
#     if a not in lista:
#         if valores == 0:
#             lista.append(a)
#         elif a > lista[-1]:
#             lista.append(a)
#         else:
#             pos = 0
#             while pos < len(lista):
#                 if a <= lista[pos]:
#                     lista.insert(pos, a)
#                     break
#                 pos += 1
#         valores += 1
#     else:
#         print(f'Valor duplicado! o valor {a} já foi digitado.')
# print(f'A sua lista em ordem númerica é {lista}.)')
# print('FIM')

# Segunda forma de fazer

lista = []
for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print(f'A sua lista em ordem númerica é {lista}.)')
print('FIM')

# # Anáslise de dados em uma tupla
#
# # Primeira maneira de fazer
#
# n1 = int(input('Digite o primeiro número: '))
# n2 = int(input('Digite o segundo número: '))
# n3 = int(input('Digite o terceiro número: '))
# n4 = int(input('Digite o quarto número: '))
#
# cont = 0
# tupla = (n1, n2, n3, n4)
# print(f'Você digitou os valores {tupla})')
# for x in tupla:
#     if x == 9:
#         cont += 1
# print(f'O valor 9 apareceu {cont} vezes.')
#
# if 3 in tupla:
#     print(f'O valor 3 apareceu em {tupla.index(3) + 1}ª posição.')
# else:
#     print('O valor 3 não fora digitado.')
#
# print('Os números pares são: ', end='')
# for x in tupla:
#     if x % 2 == 0:
#        print(x, end=" ")

# Segunda maneira de fazer

num = (int(input('Digite o primeiro número: ')),
       (int(input('Digite o segundo número: '))),
       (int(input('Digite o terceiro número: '))),
       (int(input('Digite o quarto número: '))))
print(f'Você digitou os números {num}.')
print(f'O valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'o valor 3 apareceu na {num.index(3) + 1}ª posição.')
else:
    print('O valor 3 não fora digitado.')
print('Os números pares são: ', end='')
for x in num:
    if x % 2 == 0:
        print(x, end=" ")

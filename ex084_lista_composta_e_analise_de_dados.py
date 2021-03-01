# Lista composta e análise de dados

# Primeira forma de fazer

# totalpessoas = []
# pessoa = []
# maispesadas = []
# maisleves = []
#
# maiorpeso = menorpeso = 0
# while True:
#     pessoa.append(str(input('Digite o nome: ')))
#     pessoa.append(int(input('Digite o peso: ')))
#     totalpessoas.append(pessoa[:])
#     if menorpeso == 0:
#         maisleves.append(pessoa[:])
#         menorpeso += 1
#
#     elif pessoa[-1] < maisleves[-1][-1]:
#         maisleves.clear()
#         maisleves.append(pessoa[:])
#     elif pessoa[-1] == maisleves[-1][-1]:
#         maisleves.append(pessoa[:])
#     if maiorpeso == 0:
#         maispesadas.append(pessoa[:])
#         maiorpeso += 1
#     elif pessoa[-1] > maispesadas[-1][-1]:
#         maispesadas.clear()
#         maispesadas.append(pessoa[:])
#     elif pessoa[-1] == maispesadas[-1][-1]:
#         maispesadas.append(pessoa[:])
#     pessoa.clear()
#     opcao = ' '
#     while opcao not in 'NS':
#         opcao = str(input('Deseja digitar outro número? (s / n) ')).strip().upper()
#     if opcao in 'Nn':
#         break
# print(f'Foram cadastradas {len(totalpessoas)} pessoas.')
# print(f'O menor peso foi {maisleves[0][1]:.2f}. Peso de ', end='')
# totalleves = len(maisleves)
# for x in range(0, totalleves):
#     print(maisleves[x][0], end=' ')
# print('')
# print(f'O maior peso foi {maispesadas[0][1]:.2f}. Peso de ', end='')
# totalpesada = len(maispesadas)
# for x in range(0, totalpesada):
#     print(maispesadas[x][0], end=' ')

# Segunda forma de fazer

temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? (S/N)'))
    if resp in 'Nn':
        break
print(f'Ao todo, você cadastrou {len(princ)} pessoas')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end=' ')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}]', end='')
print()
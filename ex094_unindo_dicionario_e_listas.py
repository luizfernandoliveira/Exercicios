"Ex094 Unindo dicionários e listas"

# Primeira forma de fazer
'''
contatos = []
pessoa = {'nome': '', 'sexo': '', 'idade': ''}
opcao = ''
while True:
    while True:
        pessoa['nome'] = str(input('nome: '))
        if pessoa['nome'] == '':
            print('Digite um nome.')
        else:
            break
    while True:
        sexo = str(input('sexo (M ou F): ')).upper()[0]
        if sexo in 'MF':
            pessoa['sexo'] = sexo
            break
        print('Opção inválida. Digite apenas F ou M.')
    pessoa['idade'] = int(input('Idade: '))
    contatos.append(pessoa.copy())


    while True:
        opcao = str(input('Deseja continuar? (S/N)')).upper()
        if opcao in 'NS' and opcao != '' :
            break
        else:
            print('Opção inválida. Digite S ou N.')
        opcao = ''
    if opcao == 'N':
        break

print('-' * 30)
print(f'{len(contatos)} foram cadastradas.')
soma = media = 0
for k, v in enumerate(contatos):
    soma += contatos[k]['idade']
media = soma/len(contatos)
print(f'A média das pessoas é de {media:.2f} anos.')
print('As mulheres cadastradas foram', end=' ')
for a, b in enumerate(contatos):
    if contatos[a]['sexo'] == 'F':
         print(contatos[a]['nome'], end=' ')
print()
for c in contatos:
    if c['idade'] >= media:
        for d, e in c.items():
            print(f'{d} = {e}; ', end='')
        print()
print('-' * 30)
'''

# Segunda forma de fazer

galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: (M/F) ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? (S/N) ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end=' ')
print()
print('D) Lista de pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('      ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end="")
        print()
print('FIM')



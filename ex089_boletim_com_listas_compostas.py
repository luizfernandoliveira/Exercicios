# Boletim com listas compostas

# Primeira foram de fazer
'''
serie = []
aluno = []
opcao = ' '
while True:
    nome = str(input('Nome do aluno: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    aluno.append(nome)
    aluno.append(n1)
    aluno.append(n2)
    media = (n1 + n2) / 2
    aluno.append(media)
    serie.append(aluno[:])
    aluno.clear()
    opcao = ' '
    while opcao not in 'NS':
        opcao = str(input('Deseja cadastrar outro aluno? (s / n) ')).strip().upper()
    if opcao in 'Nn':
        break
print('=' * 30)
print('ID   ', 'Nome          ', 'Média')
print('-' * 30)
for x in range(0, len(serie)):
    print(f'{x:<1}     {serie[x][0]:15}{serie[x][3]:>1}')
print('-' * 30)

opcao2 = 0
while True:
    opcao2 = int(input('Mostrar notas do aluno? Digite o número correspondente (999 para sair): '))
    if opcao2 == 999:
        break
    if opcao2 <= len(serie) - 1:
        print(f'Notas de {serie[opcao2][0]} são {serie[opcao2][1:3]}.')
    else:
        print('Valor inválido. Digite o número corretamente: ')
print('FIM')
'''

# Segunda foram de fazer

ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? (S/N) '))
    if resp in 'Nn':
        break
print('=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA:8"}')
print('-' * 30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:8.1f}')
while True:
    print('-' * 30)
    opc = int(input('Mostrar nota de qual aluno? (999 para sair): '))
    if opc == 999:
        print('Finalizado...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<<< Volte Sempre >>>>')

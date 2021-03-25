"Ex095 Aprimorando os dicionários"

# Primeira forma de fazer
'''
times = []
jogador = dict()
partidas = list()
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, tot):
        partidas.append(int(input(f"    Quantos gols na partida {c+1}? ")))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    times.append(jogador.copy())
    jogador.clear()
    partidas.clear()
    while True:
        resp = str(input('Quer continuar? (S/N) ')).upper()[0]
        if resp in 'NS':
            break
    if resp == 'N':
        break
print('-' * 30)
print('cod nome          gols           total   ')
for k, v in enumerate(times):
    print(f'{k:>3} {times[k]["nome"]:<4}          {times[k]["gols"]}         {times[k]["total"]}')
print('-' * 30)
dados = 0
print(times)
while dados != 999:
    dados = int(input('Mostrar dados de qual jogador? (999 para sair) '))
    if dados < len(times):
        print(f'LEVANTAMENTO DO JOGADOR "{times[dados]["nome"]}"')
        for i, v in enumerate(times[dados]['gols']):
            print(f'No jogo {i + 1} fez {v} gols.')
    else:
        if dados == 999:
            break
        else:
            print('Código inválido! Digite o código do jogador.')
print('FIM')
'''

# Segunda forma de fazer

time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f"    Quantos gols na partida {c+1}? ")))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? (S/N) ')).upper()[0]
        if resp in 'NS':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR "{time[busca]["nome"]}":')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')
